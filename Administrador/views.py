from django.shortcuts import render, redirect, get_object_or_404
from Cliente.models import *
from datetime import date
from django.db.models import Sum, F
from django.contrib.auth.hashers import make_password
from Administrador import utils

def index(request):
    mod = []
    calCurrent = utils.buildCalendar(date.today())
    currentYear = date.today().year
    label = Orden.objects.filter(fecha__year= currentYear)
    mod.extend(utils.buildLabel())
    return render(request, 'Administrador/index.html', {"cal": calCurrent, "fechas": label, "año": currentYear, "mod": mod})


def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')

def agregarProducto(request):
    return render(request, 'Administrador/agregarProducto.html')

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

    if usuario.is_active:
        usuario.is_active = 0
    else:
        usuario.is_active = 1

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