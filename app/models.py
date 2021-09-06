from django.db import models
from django.db.models.fields import DateField
import datetime
# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=64)
    cantidad=models.IntegerField()
    fecha_compra=models.DateField()
    precio_costo=models.FloatField()
    precio_venta=models.FloatField()
    
    #hay que desconectar del stock la cantidad vendida
    def ActualizarStock(self,cantidad):
        self.cantidad=self.cantidad-cantidad
        self.save()

    def __str__(self):
        return f"{self.nombre}"

class Servicio(models.Model):
    nombre=models.CharField(max_length=64)
    precio_venta=models.FloatField()

    def __str__(self):
        return self.nombre

class VentaServicio(models.Model):
    fecha=models.DateField()
    servicio=models.CharField(max_length=64) 
    ganancia=models.FloatField(default=1)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.fecha}-{self.ganancia}"

class VentaProducto(models.Model):
    fecha_venta=models.DateField(default=datetime.date.today)
    producto=models.CharField(max_length=64)
    ganancia=models.FloatField(default=1)
    cantidad=models.IntegerField(default=1)

    def CalcularVenta(self,cantidad,precio_venta,fecha):
        self.ganancia+=precio_venta*cantidad
        self.cantidad=cantidad
        self.fecha_venta=fecha
        self.save()
        

    def __str__(self):
        return f"{self.fecha_venta}-{self.ganancia}"