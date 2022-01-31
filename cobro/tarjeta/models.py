
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Cliente(models.Model):
    identificacion = models.BigIntegerField(primary_key=True)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    nombres = models.CharField(max_length=100, blank=False, null= False)

    def __str__(self):
        text = '{0} {1}'
        return text.format(self.apellidos, self.nombres)
    


class Pagaduria(models.Model):
    codigo = models.BigIntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        text = '{0}'
        return text.format(self.nombre)

class Empresa(models.Model):
    identificacion = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        text = '{0}'
        return text.format(self.nombre)


class Banco(models.Model):
    nombre =models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        text = '{0}'
        return text.format(self.nombre)

class Responsable(models.Model):
    identificacion = models.BigIntegerField(primary_key= True)
    empleado =  models.CharField(max_length=100, blank=False, null= False)

class Rtarjeta(models.Model):
    n_tarjeta = models.BigIntegerField()
    clave = models.CharField(max_length=4)
    cliente = models.ForeignKey(Cliente, blank=False, null=False, on_delete=models.CASCADE)
    pagaduria= models.ForeignKey(Pagaduria,blank=False, null=False, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, blank=False, null=False, on_delete=models.CASCADE)
    cuota = models.BigIntegerField(null=True, blank=True)
    


