from calendar import HTMLCalendar
import calendar
from datetime import date
from Cliente.models import *


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


def buildLabel():
    mes = 1
    data = []
    for x in range(11):
        mod = Orden.objects.filter(fecha__year = date.today().year, fecha__month=mes).count()
        data.append(mod)
        mes += 1
    return data
