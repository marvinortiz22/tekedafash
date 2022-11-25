from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, F
from Cliente.decorators import *
from .models import *
from Administrador.models import Usuario, Prenda, Talla
import re
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from .forms import PerfilForm
from django.db.models import Q


def index(request):
    request.session['carrito'] = []
    return render(request, 'Cliente/index.html')


def miCarrito(request):
    return render(request, 'Cliente/carritoCompras.html')


@usuarioAutenticado
def iniciarSesion(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        usuario = authenticate(
            request, username=nombreUsuario, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            if (usuario.is_staff):
                return redirect('/dashboard')
            else:
                return redirect('/')
        else:
            messages.error(request, "¡Usuario o contraseña incorrectas!")
            return render(request, 'Cliente/iniciarSesion.html')
    return render(request, 'Cliente/iniciarSesion.html')


@login_required(login_url='iniciarSesion')
def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')


def misCompras(request):
    ordenes = DetalleDeOrden.objects.filter(orden__cliente_id=request.user.id).values(
        'orden_id', 'orden__fecha').annotate(total=Sum(F('precio') * F('cantidad')))
    contexto = {"ordenes": ordenes}
    return render(request, 'Cliente/misCompras.html', contexto)


def detalledemiCompra(request, id):
    orden = get_object_or_404(Orden, id=id, cliente_id=request.user.id)
    ventas = DetalleDeOrden.objects.filter(orden=orden)
    monto = 0
    for venta in ventas:
        monto += venta.precio*venta.cantidad
    return render(request, 'Cliente/detalledemiCompra.html', {"ventas": ventas, "orden": orden, "monto": monto})


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
    expr = re.compile('\d{9}')
    ob = expr.match(dui)
    if (contra == contra2 and ob):
        nueuser = Usuario.objects.create(password=make_password(contra,None,'pbkdf2_sha256'), username=user, first_name=nombre,
                                         last_name=apellido, email=correo, nacimiento=fechaNaci, documento=dui)
        login(request, nueuser)
        return redirect('/')
    else:
        if(contra != contra2):
            messages.error(request, "Las contraseñas no coinciden")
        if not(bool(ob)):
            messages.error(request, "Digite un DUI valido")
        return render(request, 'Cliente/registrarUsuario.html')


def productos(request):
    products = Prenda.objects.all().filter(visibilidad = 1).order_by('nombre')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'Cliente/productos.html', context)

def busqueda(request):
    palabra = request.GET['busc']
    if palabra:
        resultados = Prenda.objects.filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
        numResultados = resultados.count()
        context = {
            'products': resultados,
            'product_count': numResultados,
        }
        return render(request, 'Cliente/productos.html', context)
    else:
        return redirect('productos')


def detalleProducto(request, id):
    prenda = Prenda.objects.get(id=id)
    tallas = Inventario.objects.filter(prenda_id = id).values('id','talla__nombre').exclude(cantidad = 0) 
    return render(request, 'Cliente/detalleProducto.html', {'prenda': prenda, 'tallas': tallas})


def editarPerfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Perfil')
    else:
        form = PerfilForm(instance=request.user)
        if request.user.is_staff == 1:
            template = "Administrador/editarPerfil.html"
        else:
            template = "Cliente/editarPerfil.html"
        return render(request, template, {"form": form})


def Perfil(request):
    if request.user.is_staff == 1:
        template = "Administrador/Perfil.html"
    else:
        template = "Cliente/Perfil.html"
    return render(request, template, {"usuario": request.user})


def cambiarContraseña(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciarSesion')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'Cliente/cambiarContraseña.html', {"form": form})


def quieneSomos(request):
    return render(request, 'Cliente/quieneSomos.html')
