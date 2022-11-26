from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "reporte"),
    path('Inventario', views.InventarioPDF.as_view(), name = "Inventario"),
    path('ListadoCliente', views.ListadoClientePDF.as_view(), name = "ListadoCliente"),
    path('ListadoProducto', views.ListadoProductoPDF.as_view(), name = "ListadoProducto"),
    path('ListadoVenta', views.ListadoVentaPDF.as_view(), name = "ListadoVenta"),
    path('Ganancias', views.GananciasPorProductoPDF.as_view(), name = "Ganancias"),
    path('ProductoMásVendidos', views.Top10PDF.as_view(), name = "ProductoMásVendidos"),
    path('Orden/<id>', views.DetalleVenta.as_view(), name = "Orden")
]