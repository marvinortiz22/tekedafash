from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404
from Cliente.models import *
from Cliente.decorators import *

@adminAutenticado
def index(request):
    ordenes=DetalleDeOrden.objects.values('orden_id','orden__fecha','orden__cliente__first_name','orden__cliente__last_name').annotate(total = Sum(F('precio') * F('cantidad')))
    contexto={"ordenes":ordenes}
    return render(request, 'Ventas/index.html',contexto)
@adminAutenticado
def detallesDeVenta(request,id):
    orden=get_object_or_404(Orden,id=id)
    ventas=DetalleDeOrden.objects.filter(orden=orden)

    monto=0
    for venta in ventas:
        monto+=venta.precio*venta.cantidad
    return render(request, 'Ventas/detallesDeVenta.html',{"ventas":ventas,"orden":orden,"monto":monto})