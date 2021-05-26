from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Show
from time import strftime

#This is the first page which containes the table
def index(request):
    context={
        'shows':Show.objects.all(),
    }
    return render(request,"index.html",context)
#This function will call the template which contains the add form.
def new_show(request):
    
    return render (request,"new_show.html")
#This function is to 
def show_shows_id(request, id):
    context={
            'this_show1': Show.objects.get(id=id),
        }
    return render (request,"tv_show.html",context)

def tv_show(request):

    if request.method=="POST":
        this_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"],release_date=request.POST["release_date"],description=request.POST['description'])
        context={
            'shows':Show.objects.all(),
            'this_show1': this_show,
            }
        return redirect(f'/shows/{this_show.id}')
    return redirect('/shows/new')

#Edit Functions
def edit_show(request,id):
    this_show=Show.objects.get(id=id)
    date=this_show.release_date
    context={
        'this_show1':this_show,
        'date':date.strftime('%Y-%m-%d')
    }
    return render (request,"edit.html",context)

def edit_show_id(request,id):
    context={
    'this_show1': Show.objects.get(id=id),
    }
    return render (request,"tv_show.html",context)

def tv_show_edit(request,id):
    this_show =Show.objects.get(id=id)
    # if request.method=="POST":
    this_show.title=request.POST["title"]
    this_show.network=request.POST["network"]
    this_show.release_date=request.POST["release_date"]
    this_show.description=request.POST["description"]
    this_show.save()

    context={
        'shows':Show.objects.all(),
        'this_show1': this_show,
        }
    return redirect(f'/shows/{this_show.id}')
    # return redirect(f'/shows/{this_show.id}/edit')

###Delete functions
def destroy(request,id):
    # if request.method=="POST":
        this_show1=Show.objects.get(id=id)
        this_show1.delete()
        return redirect('/shows')

