from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "ventas"),
    path('detallesDeVenta/<id>',views.detallesDeVenta, name="detalles de venta"),

]