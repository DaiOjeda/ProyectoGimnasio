from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    dni = forms.CharField(max_length=8)

class ActividadFormulario(forms.Form):
  nombre = forms.CharField(max_length=40)
  dni = forms.CharField(max_length=8)