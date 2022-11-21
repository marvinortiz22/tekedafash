from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "dashboard"),
    path('gestionarProducto', views.gestionarProducto, name="gestionarProducto"),
    path('gestionarCliente', views.gestionarCliente, name="gestionarCliente"),
    path('ordenesCliente/<id>', views.ordenesCliente, name="ordenesCliente"),
    path('detalleOrdenCliente/<id>', views.detalleOrdenCliente, name="detalleOrdenCliente"),
    path('editarClienteActivo/<id>', views.editarClienteActivo, name="editarClienteActivo"),
    path('gestionarAdministrador', views.gestionarAdministrador, name="gestionarAdministrador"),
    path('eliminarAdmin/<id>',views.eliminarAdmin, name="eliminarAdmin"),
    path('editarAdmin/<id>',views.editarAdmin, name="editarAdmin"),
    path('cambiosAdmin/<id>', views.cambiosAdmin, name="cambiosAdmin"),
    path('crearAdmin',views.crearAdmin, name="crearAdmin"),
    path('registroAdmin', views.registroAdmin, name="registroAdmin"),
]