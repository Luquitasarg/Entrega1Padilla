from contextvars import ContextVar
from decimal import Context
from http.client import HTTPS_PORT
from re import TEMPLATE
from string import Template
from urllib.request import HTTPRedirectHandler
from django import template

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader


def inicio(request):
    return render(request,"index.html",{})


def mi_plantilla(request):
    nombre = 'Jorge'
    apellido = 'Atahualpa'
    
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'largo': len(nombre)
    }
    
    return render(request,"mi_plantilla.html",diccionario_de_datos)