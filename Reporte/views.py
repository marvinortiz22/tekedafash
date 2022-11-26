from Reporte.utils import crearPDF
from django.shortcuts import render, HttpResponse
from django.views import View
from django.db.models import Sum, F, Count
from django.utils import timezone
from Administrador.models import *
from Cliente.models import *

def index(request):
    return render(request,'Reporte/index.html')

class InventarioPDF(View):
    def get(self, request, *args, **kwargs):
        prendas = Inventario.objects.values("prenda__id","prenda__nombre").annotate(existencia=Sum('cantidad')).exclude(prenda__visibilidad = 2)
        data = []
        for prenda in prendas:
            if prenda['existencia'] > 0:
                data.append({"nombre":  prenda['prenda__nombre'], "cantidad": prenda['existencia'], "inventario": Inventario.objects.filter(prenda_id = prenda['prenda__id']).exclude(cantidad = 0)})
        pdf = crearPDF('Reporte/Inventario.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
class ListadoClientePDF(View):
    def get(self, request, *args, **kwargs):
        clientes = Usuario.objects.filter(is_staff=0).exclude(is_superuser=1).order_by('last_name')
        data = []
        for cliente in clientes:
            data.append({"nombre":  cliente.first_name, "apellido": cliente.last_name, "usuario": cliente.username , "cantidad": Orden.objects.filter(cliente_id = cliente.id).count()})
        pdf = crearPDF('Reporte/listadoCliente.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')

class ListadoProductoPDF(View):
    def get(self, request, *args, **kwargs):
        data = Prenda.objects.filter(visibilidad = 1).values("id","nombre","descripcion","precioVenta") 
        pdf = crearPDF('Reporte/listadoProducto.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class ListadoVentaPDF(View):
    def get(self, request, *args, **kwargs):
        clientes = Orden.objects.values('cliente__id','cliente__first_name','cliente__last_name').annotate(total=Count('id'))
        data = []
        for cliente in clientes:
            data.append({"nombre": cliente['cliente__first_name'] + " " + cliente['cliente__last_name'], "cantidad": cliente['total'],"ventas": DetalleDeOrden.objects.filter(orden__cliente_id = cliente['cliente__id']).values('orden__fecha').annotate(total = Sum(F('precio') * F('cantidad')))})
        pdf = crearPDF('Reporte/listadoDeVentas.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class GananciasPorProductoPDF(View):
    def get(self, request, *args, **kwargs):
        data = DetalleDeOrden.objects.values("inventario__prenda__nombre").annotate(ganancia=Sum((F('precio')-F('costo'))*F('cantidad')))
        pdf = crearPDF('Reporte/gananciasPorProducto.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')

class Top10PDF(View):
    def get(self, request, *args, **kwargs):
        data = DetalleDeOrden.objects.values("inventario__prenda__nombre").annotate(cantidad=Sum('cantidad')).order_by('-cantidad')[:10]
        pdf = crearPDF('Reporte/top10.html', {"data": data,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class DetalleVenta(View):
    def get(self, request, id, *args, **kwargs):
        orden=Orden.objects.get(id=id)
        ventas=DetalleDeOrden.objects.filter(orden=orden)
        monto=0
        for venta in ventas:
            monto+=venta.precio*venta.cantidad
        pdf = crearPDF('Reporte/detalleVentas.html', {"ventas":ventas,"orden":orden,"monto":monto,"user": request.user.first_name + " " + request.user.last_name,"date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')