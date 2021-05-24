from django.shortcuts import render,redirect
from .models import Dojo,Ninjas
# Create your views here.
def index(request):
    context={
    "xxx": Dojo.objects.all(),
    }
    return render(request,"index.html",context)

def adddojo(request):
    if request.method=='POST':
        if request.POST['add']=='dojo':
            Dojo.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST["state"])
    return redirect("/")

def addninja(request):
    if request.method=='POST':
        if request.POST['add']=='ninja':
            Ninjas.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],dojokey=Dojo.objects.get(name=request.POST['dojokey']))
    return redirect("/")