from django.urls import path
from AppFightwear.views import *

urlpatterns = [
    
    path("", padre, name="padre"),
    path("kimonos", kimonos, name="kimonos"),
    path("rashguards", rashguards, name="rashguards"),
    path("bermudas", bermudas, name="bermudas"),

]
