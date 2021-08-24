"""
    Vistas principal del Login
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def seleccion(request):
    return render(request,"plant_slc.html")

