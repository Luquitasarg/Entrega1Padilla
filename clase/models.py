from django.db import models



class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Email: {self.email}'


class Entregable(models.Model):
    nombre = models.CharField(max_length=20) 
    fechaDeEntrega = models.DateTimeField()
    entregado = models.BooleanField()


class Curso(models.Model):
    nombre = models.CharField(max_length=20) 
    camada = models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Camada: {self.camada}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Email: {self.email} - Profesión: {self.profesion}'


