from .views import inicio, mi_plantilla
from django.urls import path

urlpatterns = [
    path('',inicio, name="inicio"),
    path('mi-plantilla/', mi_plantilla, name="mi_plantilla"),
    ]