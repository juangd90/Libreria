from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView 
from .models import Producto,Servicio,VentaProducto,VentaServicio
from django.urls.base import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'app/index.html',{
    })

#todas las altas    
#agregar al final LoginRequiredMixin
class AltaProducto(LoginRequiredMixin,CreateView):
    login_url='login'
    model=Producto
    form=Producto
    fields="__all__"
    success_url= reverse_lazy('index')

class AltaServicio(LoginRequiredMixin,CreateView):
      #login_url='login'
    model=Servicio
    form=Servicio
    fields="__all__"
    success_url= reverse_lazy('index')



#todas listas
class ListaProductos(LoginRequiredMixin,ListView):
    model=Producto
    template_name="app/lista_productos.html"

class ListaServicios(LoginRequiredMixin,ListView):
    model=Servicio
    template_name="app/lista_servicios.html"

#todas edicion
class EditarProducto(LoginRequiredMixin,UpdateView):
    model=Producto
    form=Producto
    fields="__all__"
    template_name="app/editar_producto.html"
    success_url=reverse_lazy('listaproductos')

class EditarServicio(LoginRequiredMixin,UpdateView):
    model=Servicio
    form=Servicio
    fields="__all__"
    template_name="app/editar_servicios.html"
    success_url=reverse_lazy('listaservicios')

#todas eliminar
class EliminarProducto(LoginRequiredMixin,DeleteView):
    model=Producto
    form=Producto
    fields="__all__"
    success_url=reverse_lazy("listaproductos")

def Venta(request):   
 if not request.user.is_authenticated:
    return redirect('login')
 else:     
    if request.method=='POST':
        #traigo la info desde el front y con esa info busco el producto
        #con la info que traigo, genero la instancia de VentaProducto y
        #llamo al metodo para calcular la ganancia
        productos=request.POST.get('respuesta')
        cantidad=int(request.POST.get('cantidad'))
        fecha=request.POST.get('fecha')
        #agregar un control, si el stock de algun producto es 0 no debe dejar seguir, y direccionar a otra pagina
        producto,created=Producto.objects.get_or_create(nombre=productos)
        if producto.cantidad<cantidad:
            messages.error(request,"Error! Verifique el stock del producto")
            return render(request,'app/index.html',{
                
            })
        venta=VentaProducto(fecha_venta=fecha,producto=productos,ganancia=0,cantidad=cantidad)
        venta.CalcularVenta(cantidad,producto.precio_venta,fecha)
        producto.ActualizarStock(cantidad)
       #genero el listado de todas las ventas cargadas para mostrar luego de registrar la venta
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
@login_required(login_url='login')    
def ReporteProductos(request):
    total_ventas=VentaProducto.objects.order_by('fecha_venta')
    return render(request,"app/lista_ventas_prod.html",{
        'total_ventas':total_ventas
    })
@login_required(login_url='login')   
def VentaSer(request):
 if not request.user.is_authenticated:
    return redirect('login')
 else:     
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

@login_required(login_url='login')
def ReporteServicios(request):
    total_ventas=VentaServicio.objects.order_by('fecha_venta')
    return render(request,"app/lista_ventas_ser.html",{
        'total_ventas':total_ventas
    })

def logout_user(request):
    logout(request)
    return redirect("index") 

def login_user(request):
    if request.user.is_authenticated:
        return redirect('app/index.html')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
       context={}
       return render(request,'app/login.html',context)      