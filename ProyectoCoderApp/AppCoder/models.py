from django.db import models

# Create your models here.
class Curso(models.Model):
    
  nombre = models.CharField(max_length=50)
  camada = models.IntegerField()

class Estudiante(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)

class Profesor(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  profesion = models.CharField(max_length=50)

class Entregable(models.Model):

  nombre = models.CharField(max_length=50)
  fecha_entrega = models.DateField()
  entregado = models.BooleanField()

