from django.shortcuts import render,redirect
from .models import Book,Author
def index(request):
    context= {
        "xbook":Book.objects.all()
    }
    return render(request,"addbook.html",context)

# Create your views here.
def addbook(request):
    if request.method=='POST':
            Book.objects.create(title=request.POST["title"],desc=request.POST["description"])
    return redirect("/")



def addauthor(request):
    if request.method=='POST':
        Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect("/")