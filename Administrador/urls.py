from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "dashboard"),
    path('gestionarProducto', views.gestionarProducto, name = "gestionarProducto"),
    path('gestionarCliente', views.gestionarCliente, name = "gestionarCliente"),
    path('gestionarAdministrador', views.gestionarAdministrador, name = "gestionarAdministrador"),
    path('eliminarAdmin/<id>',views.eliminarAdmin, name="eliminarAdmin"),
    path('editarAdmin/<id>',views.editarAdmin, name="editarAdmin")
]