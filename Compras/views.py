from django.shortcuts import render,redirect
from django.http import JsonResponse
from Administrador.models import Prenda, Inventario

def index(request):
    prenda = Prenda.objects.all()
    return render(request, 'Compras/index.html', {"Prendas":prenda})
def obtenerTalla(request):
    if request.method == 'GET':
        inventario = Inventario.objects.filter(prenda_id= request.GET['id'])
        data = []
        for talla in inventario:
            data.append({"nombre":talla.talla.nombre,"id":talla.talla.id,"cantidad":talla.cantidad})
        return JsonResponse(data={'data':data})
    return JsonResponse(status=400)
def agregarPrendas(request):
    inventario = Inventario.objects.filter(prenda_id= request.POST['id-prenda'])
    for talla in inventario:
        talla.cantidad += int(request.POST['talla-'+ str(talla.talla.id)])
        talla.save()
    return redirect('/dashboard/compras/')
