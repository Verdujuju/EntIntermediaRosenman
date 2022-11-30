from django.urls import path
from AppFightwear.views import *

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("kimonos", kimonos, name="kimonos"),
    path("rashguards", rashguards, name="rashguards"),
    path("bermudas", bermudas, name="bermudas"),
]
