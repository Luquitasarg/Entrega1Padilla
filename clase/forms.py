from logging import PlaceHolder
from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    profesion = forms.CharField(max_length=20)
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    
class BusquedaCurso(forms.Form):
    partial_curso = forms.CharField(label='',max_length=20)
    
class BusquedaProfesor(forms.Form):
    partial_profesor = forms.CharField(label='',max_length=20)

class BusquedaEstudiante(forms.Form):
    partial_estudiante = forms.CharField(label='',max_length=20)