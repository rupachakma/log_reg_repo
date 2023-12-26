from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from app.forms import LoginForm, RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        
        form = LoginForm(request=request,data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                user_type = user.user_type
                if user_type == 'admin':
                    return HttpResponse("You are admin")
                elif user_type == 'user':
                    return HttpResponse("You are just a user")
                else:
                    return HttpResponse("Invalid User")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("login")