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
import random
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from .forms import PerfilForm
from django.db.models import Q
from django.http import JsonResponse

@clienteAutenticado
def index(request):
    num = []
    x = []
    prendas = Prenda.objects.all().filter(visibilidad = 1)
    for prenda in prendas:
        x.append(prenda.id)
    num = random.sample(x, 6)
    prendasFinales = []
    for prenda in prendas:
        if prenda.id == num[0]:
            prendasFinales.append(prenda)
        elif prenda.id == num[1]:
            prendasFinales.append(prenda)
        elif prenda.id == num[2]:
            prendasFinales.append(prenda)
        elif prenda.id == num[3]:
            prendasFinales.append(prenda)
        elif prenda.id == num[4]:
            prendasFinales.append(prenda)
        elif prenda.id == num[5]:
            prendasFinales.append(prenda)
    return render(request, 'Cliente/index.html', {"prendas":prendasFinales})

@clienteAutenticado
def miCarrito(request):
    if not request.user.is_authenticated:
        messages.info(request, "¡Inicia sesión para completar tu orden!")
    total = 0
    if 'carrito' in request.session:
        for c in request.session['carrito']:
            talla = Inventario.objects.get(id = c['tallaId'])
            if talla.cantidad < c['cantidad']:
                if talla.cantidad == 0:
                    (request.session['carrito']).remove(c)
                    request.session.modified = True
                    messages.info(request, "Se ha eliminó por falta de existencia el producto: " + str(c['nombrePrenda']) + " - "  + str(c['tallaNombre']))
                else:
                    c['cantidad'] = talla.cantidad
                    c['subtotal'] = float(c['cantidad']) * float(c['precioPrenda'])
                    messages.info(request, "Se ha modificado el producto: " + str(c['nombrePrenda']) + " - "  + str(c['tallaNombre']))
            total += c['subtotal']
        context = {"carrito":request.session['carrito'], "total":total}
    else:
        context = {"total":total}
    return render(request, 'Cliente/carritoCompras.html', context)

@clienteAutenticado
def agregarPrenda(request, id):
    if request.method == 'GET':
        request.session['carrito'] = []
    else:
        cant = int(request.POST['cant-prenda'])
        prenda = Prenda.objects.get(id = id)
        talla = Inventario.objects.get(id =request.POST['talla-prenda'])
        if 'carrito' not in request.session:
            request.session['carrito'] = []
        else:
            request.session['carrito'] = request.session['carrito']
            for item in request.session['carrito']:
                if item['prendaId'] == prenda.id and item['tallaId'] == talla.id:
                    item['cantidad'] += cant
                    item['subtotal'] = float(cant) * float(prenda.precioVenta)
                    return redirect("productos")
        subtotal = float(cant) * float(prenda.precioVenta)
        request.session['carrito'].append({
            "prendaId": prenda.id,
            "nombrePrenda":prenda.nombre,
            "precioPrenda":prenda.precioVenta,
            "urlFotoPrenda": prenda.urlFoto.url,
            "cantidad": cant,
            "subtotal":subtotal,
            "tallaId": talla.id,
            "tallaNombre": talla.talla.nombre
        })
        return redirect("productos")

@clienteAutenticado
def quitarPrenda(request, id):
    index = id - 1
    del request.session['carrito'][index]
    request.session.modified = True
    messages.info(request, "¡El producto fue retirado de tu carrito!")
    return redirect("carrito")

@clienteAutenticado
def limpiarCarrito(request):
    request.session['carrito'] = []
    return redirect("productos")

@clienteAutenticado
def realizarOrden(request):
    orden = Orden.objects.create(
        cliente = request.user
    )
    if 'carrito' in request.session:
        for ca in request.session['carrito']:
            talla = Inventario.objects.get(id = ca['tallaId'])
            if talla.cantidad < ca['cantidad']:
                return JsonResponse(data={'status': 400})
        for c in request.session['carrito']:
            prenda = Prenda.objects.get(id = c['prendaId'])
            inventario = Inventario.objects.get(id = c['tallaId'])
            DetalleDeOrden.objects.create(
                costo = prenda.costo,
                precio = prenda.precioVenta,
                cantidad = c['cantidad'],
                inventario = inventario,
                orden = orden
            )
            inventario.cantidad -= int(c['cantidad'])
            inventario.save()
        request.session['carrito'] = []
        return JsonResponse(data={'ordenId': orden.id,'status': 200})
    return JsonResponse(status=400)

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

@clienteAutenticado
def misCompras(request):
    ordenes = DetalleDeOrden.objects.filter(orden__cliente_id=request.user.id).values(
        'orden_id', 'orden__fecha').annotate(total=Sum(F('precio') * F('cantidad')))
    contexto = {"ordenes": ordenes}
    return render(request, 'Cliente/misCompras.html', contexto)

@clienteAutenticado
def detalledemiCompra(request, id):
    orden = get_object_or_404(Orden, id=id, cliente_id=request.user.id)
    ventas = DetalleDeOrden.objects.filter(orden=orden)
    monto = 0
    for venta in ventas:
        monto += venta.precio*venta.cantidad
    return render(request, 'Cliente/detalledemiCompra.html', {"ventas": ventas, "orden": orden, "monto": monto})

@clienteAutenticado
def registrarse(request):
    return render(request, 'Cliente/registrarUsuario.html')

@clienteAutenticado
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

@clienteAutenticado
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

@clienteAutenticado
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

@clienteAutenticado
def detalleProducto(request, id):
    prenda = Prenda.objects.get(id=id)
    tallas = Inventario.objects.filter(prenda_id = id).values('id','talla__nombre').exclude(cantidad = 0)
    return render(request, 'Cliente/detalleProducto.html', {'prenda': prenda, 'tallas': tallas})

@usuarioAutenticado
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

@usuarioAutenticado
def Perfil(request):
    if request.user.is_staff == 1:
        template = "Administrador/Perfil.html"
    else:
        template = "Cliente/Perfil.html"
    return render(request, template, {"usuario": request.user})

@usuarioAutenticado
def cambiarContraseña(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciarSesion')
    else:
        form = PasswordChangeForm(user=request.user)
        if request.user.is_staff == 1:
            return render(request, 'Administrador/cambiarContraseña.html', {"form": form})
        else:
            return render(request, 'Cliente/cambiarContraseña.html', {"form": form})

@clienteAutenticado
def quieneSomos(request):
    return render(request, 'Cliente/quieneSomos.html')

@clienteAutenticado
def obtenerCantidadTalla(request):
    if request.method == 'GET':
        inventario = Inventario.objects.get(id = request.GET['id'])
        data = ({'cantidad': inventario.cantidad})
        return JsonResponse(data={'data':data})
    return JsonResponse(status=400)