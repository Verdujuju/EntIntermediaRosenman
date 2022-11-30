from django import forms

class FormKimonos(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=20)
    color=forms.CharField(max_length=20)
    talle=forms.CharField(max_length=10)
    precio=forms.IntegerField()

class FormBermudas(forms.Form):
    marca= forms.CharField(max_length=50)
    modelo= forms.CharField(max_length=50)
    color= forms.CharField(max_length=20)
    talle= forms.CharField(max_length=10)
    precio= forms.IntegerField()

class FormRashguards(forms.Form):
    marca= forms.CharField(max_length=50)
    modelo= forms.CharField(max_length=50)
    color= forms.CharField(max_length=20)
    talle= forms.CharField(max_length=10)
    precio= forms.IntegerField()