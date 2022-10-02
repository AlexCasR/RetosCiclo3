from ast import Import
from django.contrib import admin

# Register your models here.

from Registros.models import Empresa
from Registros.models import Empleados
from Registros.models import Usuarios
from Registros.models import Transferencias

admin.site.register(Empresa)
admin.site.register(Empleados)
admin.site.register(Usuarios)
admin.site.register(Transferencias)
