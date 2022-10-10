from django.urls import path

from Registros.views import EmpresaView, TrabajadoresView, UsersView, TransferView

urlpatterns = [
    path('Empresas/', EmpresaView.as_view(), name='Listar'),
    path('Empresas/<str:ID>', EmpresaView.as_view(), name='Buscar'),
    path('Empleados/', TrabajadoresView.as_view(), name='Listar'),
    path('Empleados/<str:IDemp>', TrabajadoresView.as_view(), name='Buscar'),
    path('Usuarios/', UsersView.as_view(), name='Listar'),
    path('Usuarios/<str:UserName>', UsersView.as_view(), name='Modificar'),
    path('Transferencias/', TransferView.as_view(), name='Registro')
]
