from django import forms

class CursoFormulario(forms.Form):
    
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

  nombre = forms.CharField(max_length=50)
  apellido = forms.CharField(max_length=50)
  email = forms.EmailField(max_length=254)
  profesion = forms.CharField(max_length=50)