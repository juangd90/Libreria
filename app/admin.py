from django.contrib import admin
from .models import Producto,Servicio,VentaProducto,VentaServicio	
# Register your models here.



class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","precio_costo","fecha_compra","precio_venta","cantidad")

class ServicioAdmin(admin.ModelAdmin):
    list_display=("nombre","precio_venta")

class VentaProductoAdmin(admin.ModelAdmin):
    list_display=("producto","fecha_venta","ganancia","cantidad")

class VentaServicioAdmin(admin.ModelAdmin):
    list_display=("servicio","fecha_venta","ganancia","cantidad")        

admin.site.register(Producto,ProductoAdmin)    
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(VentaServicio,VentaServicioAdmin)
admin.site.register(VentaProducto,VentaProductoAdmin)