from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "dashboard"),
    path('gestionarProducto', views.gestionarProducto, name = "gestionarProducto"),
    path('gestionarCliente', views.gestionarCliente, name = "gestionarCliente"),
    path('gestionarAdministrador', views.gestionarAdministrador, name = "gestionarAdministrador"),
    path('eliminarAdmin/<username>',views.eliminarAdmin, name="eliminarAdmin")
]