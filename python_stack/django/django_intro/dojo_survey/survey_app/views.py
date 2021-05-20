from django.shortcuts import render

def index(request):
    return render(request, "index.html")
# Create your views here.
def result(request):
    name=request.POST['name']
    location=request.POST['location']
    lang=request.POST['lang']
    comment=request.POST['comment']
    context={
        "name":name,
        "location":location,
        "lang":lang,
        "comment":comment,
    }
    return render(request,"result.html",context)