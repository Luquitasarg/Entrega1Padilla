from django.urls import path
from .views import busqueda_estudiante, busqueda_profesor, formulario_estudiante, formulario_profesor, nuevo_curso, formulario_curso, busqueda_curso

urlpatterns = [
    path('nuevo/', nuevo_curso, name='nuevo_curso'),
    path('agregar-curso/', formulario_curso, name='formulario_curso'),
    path('busqueda-curso/', busqueda_curso, name='busqueda_curso'),
    path('busqueda-profesor/', busqueda_profesor, name='busqueda_profesor'),
    path('agregar-profesor/', formulario_profesor, name='formulario_profesor'),
    path('busqueda-estudiante/', busqueda_estudiante, name='busqueda_estudiante'),
    path('agregar-estudiante/', formulario_estudiante, name='formulario_estudiante')
]
