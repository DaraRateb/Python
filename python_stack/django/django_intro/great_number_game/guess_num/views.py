from django.shortcuts import render,redirect
import random 	  

dumnum=random.randint(1, 100)
def start(request):
   
    return render (request,'index.html')

def guess(request):
    random=request.session['dumnum']
    context={
        'x':dumnum,
    }
    number = int(request.POST['number'])
    if number == random:
        context={
            'text':'You won, this is the number',
            'color':'green'
        }
    elif number>random:
        context={
            'text':'Too high',
            'color':'red'
        }
    elif number<random:
        context={
            'text':'Too Low',
            'color':'red'
        }
    return render(request,'result.html',context)
# Create your views here.
