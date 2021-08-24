"""
    Vista principal de un programa
"""
from django.contrib import admin
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect

# Create your views here.

def login_principal(request):
    if request.method == "POST":
        username=request.POST.get('usuario')
        password=request.POST.get('contra')
        userSession = authenticate(request,username= username,password=password)
        if userSession:
            login(request,userSession)
            if request.POST.get('usuario') == 'admin':
                return redirect("entrada")
            else:
                return redirect("homepage")
        else:
            return render(request,"plant_err.html")
    return render(request,"plant_log.html")

def logout_pag(request):
    logout(request)
    return redirect("logon")

def login_admin(request):
    return redirect("/admin/users/userprofile/add/")

#samuel_123