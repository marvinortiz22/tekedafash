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
    path('agregarProducto', views.agregarProducto, name="agregarProducto"),
    path('cambiarVisibilidad/<id>', views.cambiarVisibilidad, name="cambiarVisibilidad"),
    path('eliminarProducto/<id>', views.eliminarProducto, name="eliminarProducto"),
    path('editarProducto/<id>', views.editarProducto, name="editarProducto"),
    path('catalgoProducto', views.catalogoProducto, name="catalogoProducto"),
    path('recuperarProducto', views.recuperarProducto, name="recuperarProducto"),
    path('activarProducto/<id>', views.activarProducto, name="activarProducto"),
    path('obtenerTallas', views.obtenerTallas, name="obtenerTallas")
]