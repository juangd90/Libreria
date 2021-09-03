from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=64)
    cantidad=models.IntegerField()
    precio_costo=models.FloatField()
    precio_venta=models.FloatField()
    

    def __str__(self):
        return f"{self.nombre}"

class Servicio(models.Model):
    nombre=models.CharField(max_length=64)
    precio_venta=models.FloatField()

    def __str__(self):
        return self.nombre

class VentaServicio(models.Model):
    fecha=models.DateField()
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,blank=True)    
    ganancia=models.FloatField(default=1)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.fecha}-{self.ganancia}"

class VentaProducto(models.Model):
    fecha=models.DateField()
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True)    
    ganancia=models.FloatField(default=1)
    cantidad=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.fecha}-{self.ganancia}"