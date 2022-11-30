from django.shortcuts import render
from AppFightwear.forms import *
from AppFightwear.models import *

def inicio(request):
    return render(request, "inicio.html",{"mensaje_inicio":"Hola soy inicio"})


def rashguards(request):
    return render(request, "rashguards.html")

def bermudas(request):
    return render(request, "bermudas.html")


def kimonos(request):
    if request.method == "POST":
        informacion_tomada_formulario_kimono = FormKimonos(request.POST)
        if informacion_tomada_formulario_kimono.is_valid():
            formulario_limpia = informacion_tomada_formulario_kimono.cleaned_data
            kimono_ingresado_db = Kimonos(marca = formulario_limpia["marca"], modelo = formulario_limpia["modelo"], color = formulario_limpia["color"], talle = formulario_limpia["talle"], precio = formulario_limpia["precio"])
            kimono_ingresado_db.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Los datos han sido guardados de manera exitosa !!!!"})
    else:
        formulario_kimonos_vacio = FormKimonos()
        return render(request, "kimonos.html", {"codigo" : formulario_kimonos_vacio})