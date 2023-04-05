from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from .forms import CursoFormulario

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

