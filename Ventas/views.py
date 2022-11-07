from django.shortcuts import render, get_object_or_404
from Cliente.models import *

def index(request):
    ordenes=Orden.objects.all()
    contexto={"ordenes":ordenes}
    return render(request, 'Ventas/index.html',contexto)

def detallesDeVenta(request,id):
    orden=get_object_or_404(Orden,id=id)
    ventas=DetalleDeOrden.objects.filter(orden=orden)

    monto=0
    for venta in ventas:
        monto+=venta.precio
    return render(request, 'Ventas/detallesDeVenta.html',{"ventas":ventas,"orden":orden,"monto":monto})