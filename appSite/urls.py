from django.urls import path
from . import views


urlpatterns = [
    # FUNÇÕES DAS TELAS
    path('', views.listar_produtos, name='listar_produtos'),
    path('telaLogin/', views.telaLogin, name = 'telaLogin'),
    path('telaCadastroUsuario/', views.telaCadastroUsuario, name = 'telaCadastroUsuario'),
    path('telaCarrinho/', views.telaCarrinho, name = 'telaCarrinho'),
    path('telaCheckout/', views.telaCheckout, name = 'telaCheckout'),
    path('telaCadastroProduto/', views.telaCadastroProduto, name = 'telaCadastroProduto'),
    path('pagamento/', views.tela_pagamento, name='tela_pagamento'),
    path('base/', views.base, name = 'base'),
    path('telaRedes/', views.telaRedes, name = 'telaRedes'),
# ---------------------------------------------------------------------------------------------------------------------
    # FUNÇÕES DOS PRODUTOS
    path('listar_todos_produtos/', views.listar_todos_produtos, name='listar_todos_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name = 'cadastrar_produto'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editarProduto'),
    path('excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluirProduto'),
# ---------------------------------------------------------------------------------------------------------------------
    # FUNÇÕES DO CARRINHO
    path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover_item_carrinho/<int:produto_id>/', views.remover_item_carrinho, name='remover_item_carrinho'),
    path('finalizar_pagamento/', views.finalizar_Pagamento, name='finalizar_pagamento'),
    path('detalhes_produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
# ---------------------------------------------------------------------------------------------------------------------
    # FUNÇÕES DO USUÁRIO
    path('resistro/', views.registro, name = 'registro'),
    path('entrar/', views.entrar, name = 'entrar'),
    path('sair/', views.sair, name = 'sair'),
]
