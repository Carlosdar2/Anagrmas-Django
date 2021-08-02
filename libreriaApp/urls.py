from django.urls import path
from django.conf.urls import handler404
from django.contrib.auth.decorators import login_required
from .views import index,pagina_404
from .views import  listar_Autores, listar_categoria
#from .views import listar_libro, AgregarAutor, eliminar_pedido
#from .views import   EliminarCategoria
#from .views import AgregarLibro,AgregarPedidoCliente, EliminarPedido


#handler404 = pagina_404

urlpatterns = [
    path('', index, name='index'),
    #Clientes
    #Autores
    path('autor/', login_required(listar_Autores), name='autor'),
 #   path('agregar_autor/', login_required(AgregarAutor.as_view()), name='agregar_autor'),
 #   path('editar_autor/<int:pk>', login_required(EditarAutor.as_view()), name='editar_autor'),
 #   path('eliminar_autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),

    #Categoria
    path('categoria/', login_required(listar_categoria), name='categoria'),
]
    
