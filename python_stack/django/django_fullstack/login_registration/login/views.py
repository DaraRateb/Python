from django.shortcuts import render,redirect
from .models import Users
from . import models
from django.contrib import messages
import bcrypt



# Create your views here.
def index(request):
    return render(request,"index.html")

def success(request):
    if "first_name" in request.session:
        return render(request,"success.html")
    return redirect("/")

def register(request):
    if request.method=="POST":
        if request.POST["login_type"]=="register":
            errors = Users.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                user=models.create_user(request.POST)
                if user:
                    if 'first_name' not in request.session:
                        request.session["first_name"]=user.first_name
                    return redirect("/success")
            return redirect("/")

def login(request):
        if request.method=="POST":
            if request.POST["login_type"]=="login":
                user=models.get_user(request.POST)
                if user:
                    # if request.POST["password"] == user[0].password:
                    if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                        if 'first_name' not in request.session:
                            request.session['first_name']=user[0].first_name
                    return redirect("/success")
                else:
                    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

