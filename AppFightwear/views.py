from django.shortcuts import render
from AppFightwear.forms import *
from AppFightwear.models import *

def inicio(request):
    return render(request, "inicio.html",{"mensaje_inicio":"Fight shop BJJ"})


def rashguards(request):
    if request.method == "POST":
        info_form_rashguards = FormRashguards(request.POST)
        if info_form_rashguards.is_valid():
            form_limpio = info_form_rashguards.cleaned_data
            rashguard_ingresada_db = Rashguards(marca = form_limpio["marca"], modelo = form_limpio["modelo"], color = form_limpio["color"], talle = form_limpio["talle"], precio = form_limpio["precio"])
            rashguard_ingresada_db.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Rashguard ingresada exitosamente"})
        else:
            form_vacio_rashguards = FormRashguards()
            return render(request, "rashguards.html", {"codigo" : form_vacio_rashguards})
    
    return render(request, "rashguards.html")


def bermudas(request):
    if request.method == "POST":
        info_form_bermudas = FormBermudas(request.POST)
        if info_form_bermudas.is_valid():
            form_limpio = info_form_bermudas.cleaned_data
            bermuda_ingresada_db = Bermudas(marca = form_limpio["marca"], modelo = form_limpio["modelo"], color = form_limpio["color"], talle = form_limpio["talle"], precio = form_limpio["precio"])
            bermuda_ingresada_db.save()
            return render(request, "inicio.html", {"mensaje_inicio":"bermudas ingresadas exitosamente"})
    else:
        form_vacio_bermudas = FormBermudas()
        return render(request, "bermudas.html", {"codigo" : form_vacio_bermudas})

    return render(request, "bermudas.html")


def kimonos(request):
    if request.method == "POST":
        info_form_kimono = FormKimonos(request.POST)
        if info_form_kimono.is_valid():
            form_limpio = info_form_kimono.cleaned_data
            kimono_ingresado_db = Kimonos(marca = form_limpio["marca"], modelo = form_limpio["modelo"], color = form_limpio["color"], talle = form_limpio["talle"], precio = form_limpio["precio"])
            kimono_ingresado_db.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Kimono ingresado con éxito!"})
    else:
        form_vacio_kimonos = FormKimonos()
        return render(request, "kimonos.html", {"codigo" : form_vacio_kimonos})

    return render(request, "kimonos.html")

def buscar_kimonos(request):
    return render(request, "buscar_kimonos.html", {"mensaje_busqueda":"Seleccione una marca de kimonos"})


def resultado_busqueda_kimonos(request):
    valor_url = request.GET["Marca"]
    if valor_url != "":
        if valor_url != "*":
            kimonos_filtrados = Kimonos.objects.filter(marca = valor_url)
        else:
            kimonos_filtrados = Kimonos.objects.all()
        return render(request, "resultado_busqueda.html", {"kimonos_seleccionados":kimonos_filtrados})
    else:
        return render(request, "buscar_kimonos.html", {"mensaje_busqueda": "No se encontro el kimono"})