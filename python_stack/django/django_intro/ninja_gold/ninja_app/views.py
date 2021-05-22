from django.shortcuts import render,redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session or 'activites' not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render (request,'index.html')

def process(request):

    if request.method=='POST':
        if request.POST['place']=='farm':
            x=random.randint(10,20)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['place']=='cave':
            x=random.randint(5,10)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['place']=='house':
            x=random.randint(2,5)
            request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['place']=='casino':
            x=random.randint(-50,50)
            if x >0:
                request.session['activities'].append('You have earned ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            if x<0:
                request.session['activities'].append('You have lost ' + str(x) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

    request.session['gold'] += x
    return redirect('/')