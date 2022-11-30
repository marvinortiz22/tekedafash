from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from Cliente.models import *
from datetime import date
from django.db.models import Sum, F
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from Administrador import utils
from .models import *

def index(request):
    mod = []
    calCurrent = utils.buildCalendar(date.today())
    currentYear = date.today().year
    label = Orden.objects.filter(fecha__year= currentYear)
    mod.extend(utils.buildLabel())
    return render(request, 'Administrador/index.html', {"cal": calCurrent, "fechas": label, "año": currentYear, "mod": mod})


def gestionarProducto(request):
    prenda = Inventario.objects.values("prenda_id","prenda__nombre","prenda__urlFoto","prenda__descripcion","prenda__visibilidad").annotate(existencia=Sum('cantidad')).exclude(prenda__visibilidad = 2)
    return render(request, 'Administrador/gestionarProducto.html',{
        "prendas": prenda
    })

def recuperarProducto(request):
    prenda = Prenda.objects.filter(visibilidad = 2)
    return render(request, 'Administrador/recuperarProducto.html',{
        "prendas": prenda
    })
    

def agregarProducto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        costo = request.POST['costo']
        precioVenta = request.POST['precio']
        visibilidad = 1
        if 'visibilidad' not in request.POST:
            visibilidad = 0
        urlFoto = request.FILES['foto']
        tipoPrenda = request.POST['tipo-prenda']
        prenda = Prenda.objects.create(nombre = nombre,descripcion = descripcion,costo = costo,precioVenta = precioVenta,visibilidad = visibilidad,urlFoto = urlFoto,tipoPrenda_id = tipoPrenda)
        tallas = Talla.objects.filter(tipoPrenda_id = tipoPrenda)
        for t in tallas:
            Inventario.objects.create(prenda=prenda,talla_id = t.id,cantidad = request.POST['talla-' + str(t.id)])
        return redirect("gestionarProducto")
    else:
        return render(request, 'Administrador/agregarProducto.html',{
            "tipoPrenda": TipoPrenda.objects.all() 
        })

def obtenerTallas(request):
    if request.method == 'GET':
        tallas = Talla.objects.filter(tipoPrenda_id = request.GET['id'])
        data = []
        for talla in tallas:
            data.append({"nombre":talla.nombre,"id":talla.id})
        return JsonResponse(data={'data':data})
    return JsonResponse(status=400)    

def cambiarVisibilidad(request,id):
    prenda = Prenda.objects.get(id = id)
    prenda.visibilidad = not prenda.visibilidad
    prenda.save()
    return redirect('gestionarProducto')

def eliminarProducto(request,id):
    prenda = Prenda.objects.get(id = id)
    prenda.visibilidad = 2
    prenda.save()
    return redirect('gestionarProducto')

def activarProducto(request,id):
    prenda = Prenda.objects.get(id = id)
    prenda.visibilidad = 0
    prenda.save()
    return redirect('gestionarProducto')

def editarProducto(request,id):
    prenda = Prenda.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'Administrador/editarProducto.html',{
            "prenda": prenda
        })
    else:
        prenda.nombre = request.POST['nombre']
        prenda.descripcion = request.POST['descripcion']
        if request.FILES['foto'] is not None:
            prenda.urlFoto = request.FILES['foto']
        prenda.save()
        return redirect("gestionarProducto")
        
def catalogoProducto(request):
    products = Prenda.objects.all().filter(visibilidad = 1).order_by('nombre')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'Administrador/catalogoProducto.html', context)

def gestionarCliente(request):
    usuarios = Usuario.objects.filter(is_staff=0).exclude(is_superuser=1)
    data = {
        'usuarios': usuarios
    }
    return render(request, 'Administrador/gestionarCliente.html', data)


def ordenesCliente(request, id):
    cliente = Usuario.objects.get(id=id)
    ordenes = DetalleDeOrden.objects.filter(orden__cliente_id=id).values(
        'orden_id', 'orden__fecha').annotate(total=Sum(F('precio') * F('cantidad')))
    contexto = {"cliente": cliente, "ordenes": ordenes}
    return render(request, 'Administrador/ordenesCliente.html', contexto)


def detalleOrdenCliente(request, id):
    cliente = Orden.objects.get(id=id).cliente
    orden = get_object_or_404(Orden, id=id, cliente_id=cliente.pk)
    ventas = DetalleDeOrden.objects.filter(orden=orden)
    monto = 0
    for venta in ventas:
        monto += venta.precio*venta.cantidad

    contexto = {"ventas": ventas, "orden": orden,
                "monto": monto, "cliente": cliente}
    return render(request, 'Administrador/detalleOrdenCliente.html', contexto)


def editarClienteActivo(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    return redirect('gestionarCliente')


def gestionarAdministrador(request):
    usuario = Usuario.objects.filter(is_staff=1)
    data = {
        'usuarios': usuario
    }
    return render(request, 'Administrador/gestionarAdministrador.html', data)


def eliminarAdmin(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('/dashboard/gestionarAdministrador')


def crearAdmin(request):
    return render(request, 'Administrador/crearAdmin.html')


def registroAdmin(request):
    nombreUsuario = request.POST['nombreUsuario']
    contrasena = request.POST['contrasena']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    dui = request.POST['dui']
    nacimiento = request.POST['nacimiento']

    usuario = Usuario.objects.create(
        username=nombreUsuario, password=make_password(contrasena,None,'pbkdf2_sha256'), first_name=nombre, last_name=apellido, email=email, documento=dui, nacimiento=nacimiento, is_staff=1
    )
    return redirect('/dashboard/gestionarAdministrador')


def editarAdmin(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "Administrador/editarAdmin.html", {'Usuario': usuario})


def cambiosAdmin(request, id):
    username = request.POST['txtUsername']
    password = request.POST['txtPassword']
    first_name = request.POST['txtfirst_name']
    last_name = request.POST['txtlast_name']
    email = request.POST['txtEmail']
    dui = request.POST['txtDui']


def cambiosAdmin(request, id):
    nombreUsuario = request.POST['nombreUsuario']
    contrasena = request.POST['contrasena']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    dui = request.POST['dui']
    nacimiento = request.POST['nacimiento']

    # Validar que sea el mismo campos de el metodo editarAdmin y realizar los cambios
    usuario = Usuario.objects.get(id=id)
    usuario.username = nombreUsuario
    usuario.password = contrasena
    usuario.first_name = nombre
    usuario.last_name = apellido
    usuario.email = email
    usuario.documento = dui
    usuario.nacimiento = nacimiento
    usuario.save()
    return redirect('/dashboard/gestionarAdministrador')