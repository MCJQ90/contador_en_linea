from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('<str:numero_identificacion>', views.detalle_cliente, name='detalle_cliente'),
    path('formulario_cliente/', views.formulario_cliente, name='formulario_cliente'),
]