from django.db import models

# Create your models here.

class Kimonos(models.Model):
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    talle=models.CharField(max_length=10)
    precio=models.IntegerField()


class Rashguards(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color= models.CharField(max_length=20)
    talle=models.CharField(max_length=10)
    precio=models.IntegerField()
        

class Bermudas(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color= models.CharField(max_length=20)
    talle= models.CharField(max_length=10)
    precio=models.IntegerField()





