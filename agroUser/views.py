from django.shortcuts import render

# Create your views here.

def index(request):
    mydict={
        "A":"Melvin",
        "B":"Thrissur"
    }
    return render(request,"intro.html",context=mydict)

def farmer(request):
    mydict={
        "name":"Rahul",
        "place":"Thrissur",
        "crop":"wheat"
    }
    return render(request,"farmer.html",context=mydict)    