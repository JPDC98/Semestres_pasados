from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from avion.models import costos

# Create your views here.

@login_required
def programa_avion(request):
    return render(request,"plant_avn.html") 

def mostrar_dato(request):
    datos= costos.objects.all()
    return render(request,"plant_avn.html",{"datos_all":datos})

def ingreso_avion(request):
    serv_com = request.POST["comida"]
    serv_beb = request.POST["bebida"]
    serv_pel = request.POST["pelicula"]
    cant_com = request.POST["cant1"]
    cant_beb = request.POST["cant2"]
    cant_pel = request.POST["cant3"]
    sum_clas = request.POST["clase"]
    subtota_l,descutent_o,tota_l = despliege(int(sum_clas),int(serv_com),int(serv_beb),int(serv_pel),int(cant_com),int(cant_beb),int(cant_pel))
    boleto = costos(
        subtotal= subtota_l,
        descuento = descutent_o,
        total= tota_l
    )
    boleto.save()
    return render(request,"plant_avn.html",{"sub_total":str(subtota_l),"descuent_o":descutent_o,"tota_l":str(tota_l)})
    
def despliege(cla,s_c,s_b,s_p,c_c,c_b,c_p):
    pres = [[50,35,70],[40,25,55],[25,10,25]]
    pres_op = [pres[cla][a] for a in range(3)]
    sub = s_c*pres_op[0]*c_c+s_b*pres_op[1]*c_b+s_p*pres_op[2]*c_p
    if c_c+c_b+c_p>=10 and cla>0:
            des = "10%"
            total = sub*0.90
    elif cla==0 and s_c>0 and s_b>0 and s_p>0:
        des = "5%"
        total= sub*0.95
    else:
        des = "0%"
        total = sub
    return sub,des,total