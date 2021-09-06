"""ProyectoLibreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('crearproducto', views.AltaProducto.as_view(template_name="app/alta_producto.html"),name="crearproducto"),
    path('crearservicio',views.AltaServicio.as_view(template_name="app/alta_servicio.html"),name="crearservicio"),
    path("listaproductos",views.ListaProductos.as_view(template_name="app/lista_productos.html"),name="listaproductos"),    
    path("listaservicios",views.ListaServicios.as_view(template_name="app/lista_servicios.html"),name="listaservicios"), 
    path('editarproducto/<int:pk>',views.EditarProducto.as_view(template_name="app/editar_producto.html"),name="editarproducto"),
    path('editarservicio/<int:pk>',views.EditarServicio.as_view(template_name="app/editar_servicios.html"),name="editarservicio"),
    path("listaproductos/eliminar/<int:pk>",views.EliminarProducto.as_view(),name="eliminarproducto"),
    path("ventaproducto/",views.Venta,name="venta")
    
]
