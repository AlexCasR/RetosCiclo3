#from django.shortcuts import render
from ast import Delete
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from Registros.models import Empresa
from Registros.models import Empleados
from Registros.models import Usuarios
from Registros.models import Transferencias



# Create your views here.

class EmpresaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
       
    def get(self,request,ID=""):
        if len(ID)>0:
            Empresas=list(Empresa.objects.filter(ID=ID).values())
            if len(Empresas)>0:
                datos={"Empresa":Empresas}
            else:
                datos={"Empresa":"No se encontro esa empresa."}
        else:
            Empresas=list(Empresa.objects.values())
            if len(Empresas)>0:
                datos={"mensaje":Empresas}
            else:
                datos={"mensaje":"No se encontraron empresas."}
        return JsonResponse(datos)
    
    def post(self,request):
        data=json.loads(request.body)
        RegistroEmpresa=Empresa(ID=data['ID'],Nombre=data['Nombre'],NIT=data['NIT'],Ciudad=data['Ciudad'],Direccion=data['Direccion'],Telefono=data['Telefono'],SectorProductivo=data['SectorProductivo'],FechaCreacion=data['FechaCreacion'],) 
        RegistroEmpresa.save()
        datos={"mensaje":"La empresa se registro de forma exitosa."}
        return JsonResponse(datos)
    
    def put(self,request,ID):
        data=json.loads(request.body)
        Empresas=list(Empresa.objects.filter(ID=ID).values())
        if len(Empresas)>0:
            Empr=Empresa.objects.get(ID=ID)
            Empr.Nombre=data["Nombre"]
            Empr.NIT=data["NIT"]
            Empr.Ciudad=data["Ciudad"]
            Empr.Direccion=data["Direccion"]
            Empr.Telefono=data["Telefono"]
            Empr.SectorProductivo=data["SectorProductivo"]
            Empr.FechaCreacion=data["FechaCreacion"]
            Empr.save()
            mensaje={"mensaje":"Esta empresa se actualizo de forma exitosa."}
        else:
            mensaje={"mensaje":"No se encontro la empresa"}
        return JsonResponse(mensaje)
    
    def delete(self,request,ID):
        ElimEmpr=list(Empresa.objects.filter(ID=ID).values())
        if len(ElimEmpr)>0:
            Empresa.objects.filter(ID=ID).delete()
            mensaje={"mensaje":"Esta empresa se elimino de forma exitosa."}
        else:
            mensaje={"mensaje":"No se encontro la empresa"}
            
        return JsonResponse(mensaje)
    
class TrabajadoresView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data=json.loads(request.body)
        try: 
            Empr=Empresa.objects.get(ID=data["Empresa_id"])
            RegistroTrabajador=Empleados.objects.create(IDemp=data['IDemp'],Nombre=data['Nombre'],Apellido=data['Apellido'],Email=data['Email'],Telefono=data['Telefono'],Empresa=Empr,FechaCreacion=data['FechaCreacion'])
            RegistroTrabajador.save()
            mensaje={"mensaje":"El Empleado se registro de forma exitosa."}
        except Empresa.DoesNotExist:
            mensaje={"Mensaje":"La empresa no existe"}
            
        return JsonResponse(mensaje)
    
    def put(self,request,IDemp):
        data=json.loads(request.body)
        Trabajadores=list(Empleados.objects.filter(IDemp=IDemp).values())
        if len(Trabajadores)>0:
            Empl=Empleados.objects.get(IDemp=IDemp)
            Empl.Nombre=data["Nombre"]
            Empl.Apellido=data["Apellido"]
            Empl.Email=data["Email"]
            Empl.Telefono=data["Telefono"]
            Empl.FechaCreacion=data["FechaCreacion"]
            Empl.save()
            mensajemod={"mensaje":"Este empleado se actualizo de forma exitosa."}
        else:
            mensajemod={"mensaje":"No se encontro este empleado"}
        return JsonResponse(mensajemod)
    
    def get(self,request):
        Trabajadores=list(Empleados.objects.values())
        if len(Trabajadores)>0:
            datos={"mensaje":Trabajadores}
        else:
            datos={"mensaje":"No se encontraron empleados."}
        return JsonResponse(datos)
    
class UsersView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data=json.loads(request.body)
        try: 
            Empl=Empleados.objects.get(IDemp=data["IDuser_id"])
            Empr=Empresa.objects.get(ID=data["Empresa_id"])
            RegistroUsuario=Usuarios.objects.create(UserName=data['UserName'],IDuser=Empl,Password=data['Password'],Empresa=Empr,Email=data['Email'],Roll=data['Roll'],FechaCreacion=data['FechaCreacion'])
            RegistroUsuario.save()
            mensaje={"mensaje":"El Usuario se registro de forma exitosa."}
        except Empresa.DoesNotExist:
            mensaje={"Mensaje":"La empresa no existe"}
        except Empleados.DoesNotExist:
            mensaje={"Mensaje":"La empleado no existe"}
            
        return JsonResponse(mensaje)
    
    def get(self,request):
        Users=list(Usuarios.objects.values())
        if len(Users)>0:
            datos={"mensaje":Users}
        else:
            datos={"mensaje":"No se encontraron Usuarios."}
        return JsonResponse(datos)
    
class TransferView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data=json.loads(request.body)
        try: 
            User=Usuarios.objects.get(UserName=data["Usuario_id"])
            RegistroTransferencia=Transferencias.objects.create(Concepto=data['Concepto'],Monto=data['Monto'],Usuario=User,TipoTransferencia=data['TipoTransferencia'])
            RegistroTransferencia.save()
            mensaje={"mensaje":"El registro se realizo de forma exitosa."}
        except Usuarios.DoesNotExist:
            mensaje={"Mensaje":"El usuario no existe"}
        
        
        return JsonResponse(mensaje)
    
    def get(self,request):
        Transacciones=list(Transferencias.objects.values())
        if len(Transacciones)>0:
            datos={"mensaje":Transacciones}
        else:
            datos={"mensaje":"No se encontraron Transferencias."}
        return JsonResponse(datos)
        
            