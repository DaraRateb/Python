from django.shortcuts import render,redirect
from .models import Book,Author
from . import models

def index(request):
    context= {
        "xbook":Book.objects.all()
    }
    return render(request,"addbook.html",context)

def book_details(request,id):
    xbook=Book.objects.filter(id=id)
    # xauthor=xbook.authors.all()
    context={
        "xbook":xbook,
        "xauthor":xauthor,
    }
    return render(request,"bookdetails.html",context)

# Create your views here.
def add_book(request):
    if request.method=='POST':
        models.add_book(request.POST)
    return redirect("/")



def add_author(request):
    if request.method=='POST':
        models.add_author(request.POST)
    return redirect("/")

