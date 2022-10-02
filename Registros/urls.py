from django.urls import path

from Registros.views import EmpresaView

urlpatterns = [
    path('Empresas/', EmpresaView.as_view(), name='Listar')
]
