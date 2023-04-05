from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoFormulario/', cursoFormulario, name="CursoFormulario"),
    path('busquedaCamada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
]