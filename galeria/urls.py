from django.urls import path
from galeria.views import index, cadastro_pecas, excluir_peca, excluir_detalhes_peca, editar_peca, editar_detalhes_peca, realizar_baixa_estoque

urlpatterns = [
    path('', index, name='index'),
    path('cadastro_pecas/', cadastro_pecas, name='cadastro_pecas'),
    path('excluir_peca/<int:pk>/', excluir_peca, name='excluir_peca'),
    path('excluir_detalhes_peca/<int:pk>/', excluir_detalhes_peca, name='excluir_detalhes_peca'),
    path('editar_peca/<int:pk>/', editar_peca, name='editar_peca'),
    path('editar_detalhes_peca/<int:pk>/', editar_detalhes_peca, name='editar_detalhes_peca'),
    path('realizar_baixa_estoque/<int:detalhe_id>/', realizar_baixa_estoque, name='realizar_baixa_estoque'),
]
