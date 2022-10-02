#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from Registros.models import Empresa
from Registros.models import Empleados
from Registros.models import Usuarios
from Registros.models import Transferencias


# Create your views here.

class EmpresaView(View):
    
    def get(self,request):
        Empresas=list(Empresa.objects.values())
        if len(Empresas)>0:
            datos={"mensaje":Empresas}
        else:
            datos={"mensaje":"No se encontraron empresas."}
        return JsonResponse(datos)
        
            