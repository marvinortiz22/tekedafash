import calendar
from datetime import datetime
import pytz;

from Cliente.models import *


def cambiarCalendario(objeto, cambio, cambios):
    objeto = objeto.replace(cambio, cambios)
    return objeto


def buildCalendar(fecha_actual):
    cal = calendar.LocaleHTMLCalendar(firstweekday=6, locale='es_ES').formatmonth(
        fecha_actual.year, fecha_actual.month)
    calCurrent = cambiarCalendario(
        cal, 'cellpadding="0"', 'cellpadding="6px"')
    calCurrent = cambiarCalendario(
        calCurrent, '>%i<' % fecha_actual.day, 'class="" bgcolor="#​008374" ><font color="#FFFFFF"><b>%i</b></font><' % fecha_actual.day)
    return calCurrent


def buildLabel():
    mes = 1
    data = []
    anio = datetime.now().year
    for x in range(12):    
        inicio = pytz.UTC.localize(datetime(anio, mes, 1, 0, 0, 00, 00000))
        if mes == 12:
            fin = pytz.UTC.localize(datetime(anio + 1, 1, 1, 0, 0, 00, 00000))
        else: 
            fin = pytz.UTC.localize(datetime(anio, mes + 1, 1, 0, 0, 00, 00000))
        mod = Orden.objects.filter(fecha__range=[inicio, fin]).count()
        data.append(mod)
        mes += 1
    return data
