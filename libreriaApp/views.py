from django.shortcuts import render, redirect
from django.contrib import auth 
from django.views.defaults import page_not_found
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import CreateView,DeleteView
from .models import Autores, Categorias, Libros, PedidosCliente
from .forms import AutorForm, CategoriaForm, LibroForm, PedidoClienteForm

# Create your views here.

def pagina_404(request):
    return render(request, '404.html')


def index(request):
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)
    
    return render(request, 'index.html', {'carrito':carrito}) #index.html es el template

def listar_Autores(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    autores = Autores.objects.all()
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id) #Traemos TODOS los datos de la tabla autores 

   #Modificar cuando estes modificando el admin o models
    if busqueda: #Preguntando si busqueda está llena 
        autores = Autores.objects.filter(
            Q(id_autor__icontains = busqueda) |
            Q(apellidos__icontains = busqueda) | 
            Q(nombres__icontains = busqueda)
        )
    datos = {
        'autores': autores,
        'carrito': carrito
    }
    return render(request, 'Anagramas.html', datos)

#--------------Views para Autor--------------#

class AgregarAutor(CreateView):
    model = Autores
    form_class = AutorForm
    template_name = 'modals/autor/agregar_autor.html'
    success_url = reverse_lazy('libreria:autor')

   
class EliminarAutor(DeleteView):
    model = Autores
    template_name = 'modals/autor/eliminar_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libreria:autor')


#--------------Views para Categoria--------------# 
def listar_categoria(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    categoria = Categorias.objects.all() #Traemos TODOS los datos de la tabla autores 
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)

    if busqueda: #Preguntando si busqueda está llena 
        categoria = Categorias.objects.filter(
            Q(id_categoria__icontains = busqueda) |
            Q(categoria__icontains = busqueda)
        )
    datos = {
        'categorias':categoria,
        'carrito': carrito
    }
    
    return render(request, 'categoria.html', datos)


def listar_pedido(request, user_id):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    pedido = PedidosCliente.objects.filter(id_cliente = user_id) #Traemos TODOS los datos de la tabla autores 
    carrito = PedidosCliente.objects.filter(id_cliente = request.user.id)

