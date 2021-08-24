from django.http import request
from django.http.request import host_validation_re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dentista.models import cliente_dentista
# Create your views here.

@login_required
def programa_dentist(request):
    return render(request,"plant_den.html") 

def respuesta_dent(request):
    fecha_solicitar = request.POST["fecha_con"]
    datos = cliente_dentista.objects.filter(fecha=fecha_solicitar)
    return render(request,"plant_den.html",{"fecha_dis":fecha_solicitar,"insertar":datos})


def confirma_dent(request):
    paciente = cliente_dentista(
        nombre=request.POST["nombre"],
        edad=request.POST["edad"],
        peso=request.POST["peso"],
        altura=request.POST["altura"],
        fecha=request.POST["fecha"],
        hora=request.POST["hora"]
    )
    paciente.save()
    return render(request,"plant_den.html")