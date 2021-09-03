from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
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