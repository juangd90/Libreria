from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.regex_helper import normalize
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView 
from .models import Producto,Servicio,VentaProducto,VentaServicio
from django.urls.base import reverse_lazy
# Create your views here.

def index(request):
    return render(request,'app/index.html',{
    })

#todas las altas    
#agregar al final LoginRequiredMixin
class AltaProducto(CreateView):
    #login_url='login'
    model=Producto
    form=Producto
    fields="__all__"
    success_url= reverse_lazy('index')

class AltaServicio(CreateView):
      #login_url='login'
    model=Servicio
    form=Servicio
    fields="__all__"
    success_url= reverse_lazy('index')



#todas listas
class ListaProductos(ListView):
    model=Producto
    template_name="app/lista_productos.html"

class ListaServicios(ListView):
    model=Servicio
    template_name="app/lista_servicios.html"

#todas edicion
class EditarProducto(UpdateView):
    model=Producto
    form=Producto
    fields="__all__"
    template_name="app/editar_producto.html"
    success_url=reverse_lazy('listaproductos')

class EditarServicio(UpdateView):
    model=Servicio
    form=Servicio
    fields="__all__"
    template_name="app/editar_servicios.html"
    success_url=reverse_lazy('listaservicios')

#todas eliminar
class EliminarProducto(DeleteView):
    model=Producto
    form=Producto
    fields="__all__"
    success_url=reverse_lazy("listaproductos")

def Venta(request):   
      
    if request.method=='POST':
        productos=request.POST.get('respuesta')
        cantidad=int(request.POST.get('cantidad'))
        fecha=request.POST.get('fecha')
        #agregar un control, si el stock de algun producto es 0 no debe dejar seguir, y direccionar a otra pagina
        producto,created=Producto.objects.get_or_create(nombre=productos)
        venta=VentaProducto(fecha_venta=fecha,producto=productos,ganancia=0,cantidad=cantidad)
        venta.CalcularVenta(cantidad,producto.precio_venta,fecha)
        producto.ActualizarStock(cantidad)
       
        total_ventas=VentaProducto.objects.order_by('fecha_venta')
        return render(request,"app/lista_ventas_prod.html",{
         'total_ventas':total_ventas
        })

    else:
        productos=Producto.objects.all()            
        return render(request,"app/vender_producto.html",{
            'productos':productos,
            })        

    #hay que listar las ventas
def ReporteProductos(request):
    total_ventas=VentaProducto.objects.order_by('fecha_venta')
    return render(request,"app/lista_ventas_prod.html",{
        'total_ventas':total_ventas
    })

def VentaSer(request):
    if request.method=='POST':
        servicios=request.POST.get('respuesta')
        cantidad=int(request.POST.get('cantidad'))
        fecha=request.POST.get('fecha')
     #agregar un control, si el stock de algun producto es 0 no debe dejar seguir, y direccionar a otra pagina
        servicio,created=Servicio.objects.get_or_create(nombre=servicios)
        venta=VentaServicio(fecha_venta=fecha,servicio=servicios,ganancia=0,cantidad=cantidad)
        venta.CalcularVenta(cantidad,servicio.precio_venta,fecha)
       
        total_ventas=VentaServicio.objects.order_by('fecha_venta')
        return render(request,"app/lista_ventas_ser.html",{
              'total_ventas':total_ventas   
        })
    else:
        servicios=Servicio.objects.all()            
        return render(request,"app/vender_servicio.html",{
            'servicios':servicios,
            })  


def ReporteServicios(request):
    total_ventas=VentaServicio.objects.order_by('fecha_venta')
    return render(request,"app/lista_ventas_ser.html",{
        'total_ventas':total_ventas
    })