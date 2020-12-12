from django.shortcuts import render

# Create your views here.
def menu(request):
   return render(request,'menu.html',{})


def home(request):
   return render(request,'home.html',{})

def login(request):
   return render(request,'login.html',{})

def resume(request):
    return render(request,'resume.html',{})

def vacancy(request):
   return render(request,'vacancy.html',{})

def signup(request):
   return render(request,'signup.html',{})
