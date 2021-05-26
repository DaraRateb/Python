from django.shortcuts import render,redirect
from . import models
# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        if request.POST["login_type"]=="login":
            if models.check_user(request.POST["email"],request.POST["password"]):
                request.session["first_name"]=request.POST["first_name"]
                return render(request,"welcome.html")
            else:
                return redirect("/login")
        if request.POST["login_type"]=="registration":
            models.register(request.POST["first_name"],request.POST["password"])
    return redirect("/")