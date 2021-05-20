from django.shortcuts import render,redirect
import random 	  

def dumnum(request):
    request.session['dumnum']=random.randint(1, 100)
    context={
        "random_number":request.session['dumnum']
    }
    return render (request,'index.html',context)

def guess(request):
    if request.POST['number'] == request.session['dumnum']:
       request.session['x']=0
    elif request.POST['number']-request.session['dumnum']>5:
        request.session['x']=5
    elif request.POST['number']-request.session['dumnum']<=5:
        request.session['x']=4
    elif request.session['dumnum']-request.POST['number']>5:
        request.session['x']=2
    elif request.session['dumnum']-request.POST['number']<=5:
        request.session['x']=1
    context={
        "y":request.session['x']
    }
   
    return render(request,'index.html',context)
# Create your views here.
