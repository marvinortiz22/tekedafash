from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "compras"),
    path('obtenerTalla', views.obtenerTalla, name = "obtenerTalla"),
    path('agregarCompra', views.agregarPrendas, name = "agregarCompra"),
]