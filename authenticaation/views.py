from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import login,authenticate
from django.views import View
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('menu')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{"form":form})

def Login(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('menu')
        else:
            print("Invalid username or password")
    form=AuthenticationForm()
    return render(request,template_name='login.html',context={"form":form})

