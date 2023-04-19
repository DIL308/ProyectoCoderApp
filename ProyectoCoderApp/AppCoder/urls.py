from django.contrib import admin
from django.contrib.auth.views import LogoutView
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
    path('listaProfesores/', listaProfesores, name="ListaProfesores"),
    path('crea-profesor/', crea_profesor, name="CreaProfesor"),
    path('elimina-profesor/<int:id>/', eliminarProfesor, name="EliminaProfesor"),
    path('editar-profesor/<int:id>/', editar_profesor, name="EditarProfesor"),
    path('listaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('detalleCursos/<pk>/', CursoDetail.as_view(), name="DetalleCursos"),
    path('creaCursos/', CursoCreate.as_view(), name="CreaCursos"),
    path('actualizarCursos/<pk>/', CursoUpdate.as_view(), name="ActualizaCursos"),
    path('eliminarCursos/<pk>/', CursoDelete.as_view(), name="EliminaCursos"),
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
]