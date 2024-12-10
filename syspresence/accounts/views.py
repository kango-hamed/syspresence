from .custumform import CustomAuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse


def login_user(request):
    auth_cond = 'username' in request.POST and 'password' in request.POST
    if request.method == 'POST' and auth_cond:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse("presence:dashboard"))
        else:
            messages.info(request,"Veuillez renseigner des informations correctes !")
    form = CustomAuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})
def logout_user(request):
    logout(request)
    return redirect('accounts:login')