from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Curso, Profesor, Avatar
from .forms import CursoFormulario, ProfesorFormulario, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

def inicio(request):
    
    try:
      avatar = Avatar.objects.get(user=request.user.id)
      return render(request, 'inicio.html', {'url': avatar.imagen.url})
    except:
      return render(request, "inicio.html")
    
def cursos(self):
    
    return render(self, "cursos.html")

def profesores(self):
    
    return render(self, "profesores.html")

def estudiantes(self):
    
    return render(self, "estudiantes.html")

def entregables(self):
    
    return render(self, "entregables.html")

def cursoFormulario(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
      
      miFormulario = CursoFormulario(request.POST)

      print(miFormulario)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data

          curso = Curso(nombre=data['curso'], camada=data['camada'])
          curso.save()
    
          return render(request, "inicio.html")
    
      else:
          
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    
    else:

      miFormulario = CursoFormulario()

      return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})
        

def busquedaCamada(request):

    return render(request, "busquedaCamada.html")  

def buscar(request):
    
    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)
        return render(request, "resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
    
    else:
        
      return HttpResponse(f'No enviaste info')

@staff_member_required(login_url='/app-coder/')
def listaProfesores(request):
    
  profesores = Profesor.objects.all()

  return render(request, "leerProfesores.html", {"profesores": profesores})

def crea_profesor(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
      miFormulario = ProfesorFormulario(request.POST)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data
          profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'],profesion=data['profesion'])
          profesor.save()
          
          return HttpResponseRedirect('/app-coder/')
    
      else:
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
      miFormulario = ProfesorFormulario()
      return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})


def eliminarProfesor(request, id):
   
   if request.method == 'POST':
      
      profesor = Profesor.objects.get(id=id)
      profesor.delete()

      profesores = Profesor.objects.all()
      return render(request, "leerProfesores.html", {"profesores": profesores})

def editar_profesor(request, id):
   
    print('method: ', request.method)
    print('post: ', request.POST)

    profesor = Profesor.objects.get(id=id)

    if request.method == 'POST':
      miFormulario = ProfesorFormulario(request.POST)

      if miFormulario.is_valid():
          
          data = miFormulario.cleaned_data
          # profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'],profesion=data['profesion'])
          profesor.nombre = data['nombre']
          profesor.apellido = data['apellido']
          profesor.email = data['email']
          profesor.profesion = data['profesion']
          profesor.save()
          
          return HttpResponseRedirect('/app-coder/')
    
      else:
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
      miFormulario = ProfesorFormulario(initial={
          "nombre": profesor.nombre,
          "apellido": profesor.apellido,
          "email": profesor.email,
          "profesion": profesor.profesion
      })
      return render(request, "editarFormulario.html", {"miFormulario": miFormulario, "id": profesor.id})

class CursoList(LoginRequiredMixin, ListView):
  
  model = Curso
  template_name = 'curso_list.html'
  context_object_name = 'cursos'

class CursoDetail(DetailView):
  
  model = Curso
  template_name = 'curso_detail.html'
  context_object_name = 'curso'

class CursoCreate(CreateView):
   
  model = Curso
  template_name = 'curso_create.html'
  fields = ['nombre', 'camada']
  success_url = '/app-coder/'

class CursoUpdate(UpdateView):
   
  model = Curso
  template_name = 'curso_update.html'
  fields = ('__all__')
  success_url = '/app-coder/'
  context_object_name = 'curso'

class CursoDelete(DeleteView):
   
   model = Curso
   template_name = 'curso_delete.html'
   success_url = '/app-coder/'

def loginView(request):
   
  if request.method == 'POST':
    miFormulario = AuthenticationForm(request, data=request.POST)

    if miFormulario.is_valid():
        
      data = miFormulario.cleaned_data
      usuario = data["username"]
      psw = data["password"]
      
      user = authenticate(username=usuario, password=psw)

      if user:
        login(request, user)
        return render(request, 'inicio.html', {"mensaje": f'Bienvenido {usuario}'})
      
      else:
        return render(request, 'inicio.html', {"mensaje": f'Error: datos incorrectos'})
         
    else:
      return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
  else:
    miFormulario = AuthenticationForm()
    return render(request, "login.html", {"miFormulario": miFormulario})
  

def register(request):
   
  if request.method == 'POST':
    miFormulario = UserCreationForm(request.POST)

    if miFormulario.is_valid():
        
      data = miFormulario.cleaned_data
      username = data["username"]
      miFormulario.save()
      return render(request, 'inicio.html', {"mensaje": f'Usuario {username} creado!'})
         
    else:
      return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
  
  else:
    miFormulario = UserCreationForm()
    return render(request, "registro.html", {"miFormulario": miFormulario})   

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':
      
      miFormulario = UserEditForm(request.POST, instance=request.user)

      if miFormulario.is_valid():
          data = miFormulario.cleaned_data
          # profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'],profesion=data['profesion'])
          usuario.email = data['email']
          usuario.first_name = data['first_name']
          usuario.last_name = data['last_name']
          usuario.set_password(data["password1"])
          usuario.save()
          
          return render(request, "inicio.html", {"mensaje": "Datos actualizados!"})
    
      else:
          return render(request, "inicio.html", {"miFormulario": miFormulario})
    else:
      miFormulario = UserEditForm(instance=request.user)
      return render(request, "editarPerfil.html", {"miFormulario": miFormulario})



@login_required
def agregar_avatar(request):
   
  print(request.POST)
  print(request.FILES)

  if request.method == 'POST':
    miFormulario = AvatarFormulario(request.POST, request.FILES)

    if miFormulario.is_valid():
        
      data = miFormulario.cleaned_data
      avatar = Avatar(user=request.user, imagen=data["imagen"])
      avatar.save()

      return render(request, 'inicio.html', {"mensaje": f'Avatar agregado!'})
         
    else:
      return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
  
  else:
    miFormulario = AvatarFormulario()
    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})
