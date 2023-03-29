from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso(self, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
      <p>Curso: {curso.nombre} - Camada: {curso.camada} creado!</p>
    """)

def lista_cursos(self):
    
    lista = Curso.objects.all()

    return render(self, "lista_cursos.html", {"lista_cursos": lista})

def inicio(self):
    
    return render(self, "inicio.html")

def cursos(self):
    
    return render(self, "cursos.html")

def profesores(self):
    
    return render(self, "profesores.html")

def estudiantes(self):
    
    return render(self, "estudiantes.html")

def entregables(self):
    
    return render(self, "entregables.html")
