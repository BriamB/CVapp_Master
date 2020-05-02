from django.db import models
from django.contrib.auth.models import User
import datetime

# Creacion de la base de datos
#Modelo departamento
class Departamento(models.Model):
    departamento = models.CharField(max_length=20)
    def __str__(self):
        return self.departamento

#Modelo Municipio
class Municipio(models.Model):
    municipio= models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.municipio

#Modelo Area
class Area(models.Model):
    Areas = models.CharField(max_length=15)

    def __str__(self):
        return self.Areas

#Modelo tipo de identificacion
class Tipo_Identificacion(models.Model):
    Tipo_identificacion = models.CharField(max_length=20)

    def __str__(self):
        return self.Tipo_identificacion

#Modelo cargo
class Cargo(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion

#Modelo de las hojas de vida
class carga_cv(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_identificacion = models.ForeignKey(Tipo_Identificacion, null=False, on_delete=models.PROTECT)
    cedula = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    genero = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    municipio = models.ForeignKey(Municipio, null=False, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=50)
    Centro_educativo = models.CharField(max_length=50)
    Nivel_educativo = models.CharField(max_length=20)
    Estado_estudio = models.CharField(max_length=10)
    Periodo_inicio = models.DateField(default=datetime.datetime.now())
    Periodo_fin = models.DateField(default=datetime.datetime.now())
    cargo = models.ForeignKey(Cargo, null=False, on_delete=models.PROTECT)
    Empresa = models.CharField(max_length=50)
    Periodo_inicio = models.DateField(default=datetime.datetime.now())
    Periodo_fin = models.DateField(default=datetime.datetime.now())
    Funciones = models.CharField(max_length=200)
    idioma = models.CharField(max_length=20)
    nivel = models.CharField(max_length=10)
    area = models.ForeignKey(Area, null=False, on_delete=models.PROTECT)
    salario = models.IntegerField()
    foto = models.FileField(null=True, upload_to="Foto/%Y/%m/%d")
    archivo_cv = models.FileField(null=True, upload_to="Cv/%Y/%m/%d")
    def __str__(self):
        return self.cedula
