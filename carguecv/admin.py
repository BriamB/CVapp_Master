from django.contrib import admin
#Se importan los modelos de la base de datos
from .models import Departamento, Municipio, Area, Tipo_Identificacion, Cargo, carga_cv

#Se asignan al django para ser visibles en la plataforma admin
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Area)
admin.site.register(carga_cv)
admin.site.register(Cargo)
