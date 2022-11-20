from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum,F
from Cliente.decorators import * 
from .models import *
from Administrador.models import Usuario, Prenda, Talla 
import re

def index(request):
    request.session['carrito'] = []
    return render(request, 'Cliente/index.html')

@usuarioAutenticado
def iniciarSesion(request):
    if request.method == 'POST':
            nombreUsuario = request.POST.get('usuario')
            contraseña = request.POST.get('contraseña')
            usuario = authenticate(request, username = nombreUsuario, password = contraseña)
            if usuario is not None:
                login(request, usuario)
                if (usuario.is_staff):
                    return redirect('/dashboard')
                else:
                    return redirect('/') 
            else:
                messages.error(request, "¡Usuario o contraseña incorrectas!")
                return render(request,'Cliente/iniciarSesion.html' )
    return render(request, 'Cliente/iniciarSesion.html')

@login_required(login_url='iniciarSesion')
def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')

def misCompras(request):
    ordenes=DetalleDeOrden.objects.filter(orden__cliente_id = request.user.id).values('orden_id','orden__fecha').annotate(total = Sum(F('precio') * F('cantidad')))
    contexto={"ordenes":ordenes}
    return render(request, 'Cliente/misCompras.html',contexto)

def detalledemiCompra(request,id):
    orden=get_object_or_404(Orden,id=id,cliente_id = request.user.id)
    ventas=DetalleDeOrden.objects.filter(orden=orden)
    monto=0
    for venta in ventas:
        monto+=venta.precio*venta.cantidad
    return render(request, 'Cliente/detalledemiCompra.html',{"ventas":ventas,"orden":orden,"monto":monto})

def registrarse(request):
    return render(request, 'Cliente/registrarUsuario.html')

def regisUsuario(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    correo = request.POST['correo']
    fechaNaci = request.POST['fechaNacimiento']
    dui = request.POST['dui']
    contra = request.POST['contraseña']
    contra2 = request.POST['contraseña2']
    user = request.POST['user']
    expr = re.compile('\d{8}-\d')
    ob = expr.match(dui)
    if (contra == contra2 and ob):
        nueuser = Usuario.objects.create(password = contra, username = user, first_name = nombre, last_name = apellido, email = correo, nacimiento = fechaNaci, documento = dui)
        return redirect('inicio')            
    else:
        if(contra != contra2):
            messages.error(request, "Las contraseñas no coinciden")
        if not(bool(ob)):
            messages.error(request, "Digite un DUI valido")
        return render(request, 'Cliente/registrarUsuario.html')

def productos(request):
    variable = Prenda.objects.all()
    return render(request, 'Cliente/productos.html', {'objetos': variable})

def detalleProducto(request, id):
    prenda = Prenda.objects.get(id=id)
    tallas = Talla.objects.all()
    return render(request,'Cliente/detalleProducto.html', {'prenda': prenda, 'tallas': tallas})