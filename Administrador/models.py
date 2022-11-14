from django.db import models
from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    documento = models.CharField(max_length=9,null=False,unique=True)
    nacimiento = models.DateField(null=False)            
    
class TipoPrenda(models.Model):
    nombre = models.CharField(max_length=60,null=False,unique=True)
    class Meta:
        db_table = "tipoPrenda"
class Talla(models.Model):
    nombre = models.CharField(max_length=60,null=False)
    tipoPrenda = models.ForeignKey(TipoPrenda,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table = "talla"
        unique_together = ('nombre', 'tipoPrenda')
class Prenda(models.Model):
    nombre = models.CharField(max_length=60,null=False)
    descripcion = models.CharField(max_length=120,null=False)
    costo = models.FloatField(null=False)
    precioVenta = models.FloatField(null=False)
    visibilidad = models.IntegerField(null=False)
    urlFoto = models.CharField(max_length=400,null=False)
    tipoPrenda = models.ForeignKey(TipoPrenda,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table = "prenda"
        unique_together = ('nombre', 'descripcion','urlFoto','tipoPrenda')
class Inventario(models.Model): 
    cantidad = models.IntegerField(null=False, default = 0)
    prenda = models.ForeignKey(Prenda,on_delete=models.CASCADE,null=False)
    talla = models.ForeignKey(Talla,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table = "inventario"
        unique_together = ('prenda','talla')