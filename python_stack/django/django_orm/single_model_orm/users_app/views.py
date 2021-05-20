from django.shortcuts import render,redirect
from .models import Users

def form(request):
    context = {
        "Guys": Users.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    Users.objects.create(firstname=request.POST["firstname"],
    last_name=request.POST["last_name"],email_address=request.POST["email_address"],age=int(request.POST["age"]))
    return redirect("/")