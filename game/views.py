from django.shortcuts import redirect, render
from datetime import datetime
import random

# Create your views here.
def index(request):
	if not 'gold' in request.session:
		request.session["gold"] = 0
		request.session['log']=[]
	context={
		"gold":request.session.get('gold'),
		"log_list":request.session['log'],
	}
	return render(request, 'game/home.html', context)

def process_money(request):
	if request.method == 'POST':
		gold=request.session.get('gold')
		action_result=0
		type_result=""
		text=""
		time=datetime.now().strftime("(%Y/%m/%d %H:%M %p)")
		if request.POST.get('actions') == "farm":
			action_result = random.randint(10,20)
			gold+=action_result
			type_result="won"
			text= "Earned "+ str(action_result) +" golds from the farm! "+ time
		if request.POST.get('actions') == "cave":
			action_result = random.randint(5,10)
			gold+=action_result
			type_result="won"
			text= "Earned "+ str(action_result) +" golds from the cave! "+ time
		if request.POST.get('actions') == "house":
			action_result = random.randint(2,5)
			gold+=action_result
			type_result="won"
			text= "Earned "+ str(action_result) +" golds from the house! "+ time
		if request.POST.get('actions') == "casino":
			action_result = random.randint(-50,50)
			gold+=action_result
			if action_result >0:
				type_result="won"
				text="Entered a casino and won "+ str(action_result) +" golds ...yay!! "+ time
			else:
				type_result="lost"
				text="Entered a casino and lost "+ str(-action_result) +" golds ...Ouch "+ time
		request.session['log'].append({
			"type": type_result,
			"text": text 
		})
		if gold <0:
			gold=0
		request.session["gold"] = gold
	return redirect('/')
