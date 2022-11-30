from django.urls import path
from AppFightwear.views import *

urlpatterns = [
    
    path("inicio", inicio, name="inicio"),
    path("kimonos", kimonos, name="kimonos"),
    path("rashguards", rashguards, name="rashguards"),
    path("bermudas", bermudas, name="bermudas"),
    path("buscar_kimonos", buscar_kimonos, name="buscar_kimonos"),
    path("resultado_busqueda", resultado_busqueda_kimonos, name="resultado_busqueda_kimonos"),


]
