from django.shortcuts import render
from Cliente.models import *
from django.shortcuts import redirect
from datetime import date
from calendar import HTMLCalendar
import calendar


def index(request):
    calCurrent = buildCalendar(date.today())
    currentYear = date.today().year
    label = Orden.objects.filter(fecha__range=(
        date(2020, 1, 1), date(2022, 11, 11)))
    return render(request, 'Administrador/index.html', {"cal": calCurrent, "fechas": label, "año": currentYear})


def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')


def gestionarCliente(request):
    return render(request, 'Administrador/gestionarCliente.html')


def gestionarAdministrador(request):
    usuario = Usuario.objects.filter(is_staff=1)
    data = {
        'Usuario': usuario
    }
    return render(request, 'Administrador/gestionarAdministrador.html', data)


def eliminarAdmin(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('/dashboard/gestionarAdministrador')


def editarAdmin(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "Administrador/editarAdmin.html", {"usuario": usuario})


def cambiarCalendario(objeto, cambio, cambios):
    objeto = objeto.replace(cambio, cambios)
    return objeto


def buildCalendar(fecha_actual):
    cal = calendar.LocaleHTMLCalendar(firstweekday=6, locale='es').formatmonth(
        fecha_actual.year, fecha_actual.month)
    calCurrent = cambiarCalendario(
        cal, 'cellpadding="0"', 'cellpadding="6px"')
    calCurrent = cambiarCalendario(
        calCurrent, '>%i<' % fecha_actual.day, 'class="" bgcolor="#​008374" ><font color="#FFFFFF"><b>%i</b></font><' % fecha_actual.day)
    return calCurrent
