from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso, Estudiante, Profesor
from clase.forms import BusquedaCurso, BusquedaEstudiante, BusquedaProfesor, CursoFormulario, ProfesorFormulario,EstudianteFormulario
from django.template import Context, Template, loader
import random

# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500,3000)
    nuevo_curso = Curso(nombre='Curso Python', camada = camada)
    nuevo_curso.save()
    return HttpResponse(f'Se creó el curso {nuevo_curso.nombre}, camada {nuevo_curso.camada}')

def formulario_curso(request):
    
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST) 
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre= data['curso'] , camada = data['camada'])
            nuevo_curso.save()
            return render(request, 'index.html',{'nuevo_curso': nuevo_curso})
        
    formulario = CursoFormulario()
    return render(request, 'formulario_curso.html',{'formulario': formulario})



def formulario_profesor(request):
    
    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST) 
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_profesor = Profesor(nombre= data['nombre'] , apellido = data['apellido'] , email = data['email'] , profesion = data['profesion'])
            nuevo_profesor.save()
        
    formulario = ProfesorFormulario()
    return render(request, 'formulario_profesor.html',{'formulario': formulario})


def formulario_estudiante(request):
    
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST) 
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = Estudiante(nombre= data['nombre'] , apellido = data['apellido'] , email = data['email'])
            nuevo_estudiante.save()
        
    formulario = EstudianteFormulario()
    return render(request, 'formulario_estudiante.html',{'formulario': formulario})
    
    
def busqueda_curso(request):
    cursos_buscados = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        cursos_buscados = Curso.objects.filter(nombre__icontains=dato)
        
    
    buscador = BusquedaCurso()
    return render(request, "busqueda_curso.html",
                  {'buscador': buscador, 'cursos_buscados': cursos_buscados, 'dato': dato})
 
 
 
def busqueda_profesor(request):
    profesores_buscados = []
    dato = request.GET.get('partial_profesor', None)

    if dato is not None:
        profesores_buscados = Profesor.objects.filter(nombre__icontains=dato) 
        
    buscador = BusquedaProfesor()
    return render(request, "busqueda_profesor.html",
                    {'buscador': buscador, 'profesores_buscados': profesores_buscados, 'dato': dato})


def busqueda_estudiante(request):
    estudiantes_buscados = []
    dato = request.GET.get('partial_estudiante', None)

    if dato is not None:
        estudiantes_buscados = Estudiante.objects.filter(nombre__icontains=dato) 
        
    buscador = BusquedaEstudiante()
    return render(request, "busqueda_estudiante.html",
                    {'buscador': buscador, 'estudiantes_buscados': estudiantes_buscados, 'dato': dato})
