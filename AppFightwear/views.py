from django.shortcuts import render

def padre(request):
    return render(request, "padre.html")

def kimonos(request):
    marca="Maeda"
    modelo="Saatsu"
    return render(request, "kimonos.html")

def rashguards(request):
    return render(request, "rashguards.html")

def bermudas(request):
    return render(request, "bermudas.html")







# Create your views here.

    