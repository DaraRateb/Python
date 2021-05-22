from django.shortcuts import render,redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    return render (request,'index.html')

def process(request):

    if request.method=='POST':
        if request.POST['place']=='farm':
            x=random.randint(10,20)
        if request.POST['place']=='cave':
            x=random.randint(5,10)
        if request.POST['place']=='house':
            x=random.randint(2,5)
        if request.POST['place']=='casino':
            x=random.randint(-50,50)

    request.session['gold'] += x
    return redirect('')