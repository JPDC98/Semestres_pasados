"""uno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uno.views import seleccion
from users.views import login_principal,logout_pag,login_admin
from avion.views import programa_avion,ingreso_avion,mostrar_dato
from dentista.views import programa_dentist,respuesta_dent,confirma_dent

urlpatterns = [
    path('admin/', admin.site.urls,name="administracion"),
    path('login/',login_principal,name="logon"),
    path('',seleccion, name="homepage"),
    path('logout/',logout_pag,name="salir"),
    path('avion/',programa_avion,name="progra2"),
    path('dentista/',programa_dentist,name="progra1"),
    path('respuestad/',respuesta_dent,name="pag_result_den"),
    path('confirmaciond/',confirma_dent,name="pag_conf_den"), 
    path('ingresoa/',ingreso_avion,name="pag_int"),
    path('salidaa/',mostrar_dato,name="pag_out"),
    path('ir/',login_admin,name="entrada")
] 

