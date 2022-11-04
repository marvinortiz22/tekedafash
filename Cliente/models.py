from django.db import models
from django.utils import timezone
from Administrador.models import Inventario,Usuario

class Orden(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)

    class Meta:
        db_table = "orden"

class DetalleDeOrden(models.Model):
    costo = models.FloatField(null=False)
    precio = models.FloatField(null=False)
    cantidad = models.FloatField(null=False)
    inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE,null=False)
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table = "detalleOrden"
        unique_together = ('orden', 'inventario')