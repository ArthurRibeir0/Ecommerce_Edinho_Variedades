from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from django.utils.translation import gettext as _
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from appSite.models import Produto
from .forms import ProdutoForm
from django.db.models import Q
from django.contrib import messages




# Telas.
def telaLogin(request):
    return render(request, 'login.html')


def telaCadastroUsuario(request):
    return render(request, 'cadastroUsuario.html')
   

def telaCarrinho(request):
    return render(request, 'carrinho.html')

@login_required
def telaCheckout(request):
    return render(request, 'checkout.html')


@login_required
def telaCadastroProduto(request):
    return render(request, 'cadastroProduto.html')


def telaRedes(request):
    return render(request, 'redesSociais.html')

@login_required
@has_role_decorator
def base(request):
    return render(request, 'base.html')



# Funcionalidades

# cadastro de usuario
def registro(request):
    if request.method == 'GET':
        # Se a solicitação for do tipo GET, renderiza o formulário de registro
        return render(request, 'cadastroUsuario.html')
    
    elif request.method == 'POST':
        # Se a solicitação for do tipo POST, processa o formulário de registro

        # Obtém os dados do formulário
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se já existe um usuário com o mesmo nome de usuário ou e-mail
        user_exists = User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()
        if user_exists:
            return HttpResponse('Já existe um usuário com esse nome de usuário ou e-mail.')

        # Cria um novo usuário usando o método create_user, que lida com a hash da senha
        user = User.objects.create_user(username=username, email=email, password=senha)

        # Salva o usuário no banco de dados
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')

    else:
        # Se o método da solicitação não for nem GET nem POST, retorna uma resposta de erro
        return HttpResponse('Método de solicitação não suportado.')



# login
def entrar(request):
    if request.method == "GET":
        # Se a solicitação for do tipo GET, renderiza o formulário de login
        return render(request, 'login.html')
    
    elif request.method == "POST":
        # Se a solicitação for do tipo POST, processa o formulário de login

        # Obtém os dados do formulário
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # Autentica o usuário usando a função authenticate do Django
        user = authenticate(request, username=username, password=senha)

        if user is not None:
            # Se o usuário for autenticado com sucesso, faz o login e redireciona para a página desejada
            login(request, user)
            return redirect('listar_produtos')  # Substitua 'telaLogado' pela URL desejada após o login
        else:
            # Se as credenciais forem inválidas, retorna uma mensagem de erro
            return HttpResponse('Nome de usuário ou senha inválidos.')

    else:
        # Se o método da solicitação não for nem GET nem POST, retorna uma resposta de erro
        return HttpResponse('Método de solicitação não suportado.')



# logout
def sair(request):
    # Realiza o logout do usuário
    logout(request)
    
    # Redireciona para a página desejada após o logout
    return redirect('telaLogin')



# cadastro de produto
def cadastrar_produto(request):
    # Inicializa o formulário vazio
    form = ProdutoForm()

    # Verifica se a requisição é do tipo POST (envio do formulário)
    if request.method == 'POST':
        # Preenche o formulário com os dados do POST e os arquivos enviados
        form = ProdutoForm(request.POST, request.FILES)

        # Exibe informações úteis para debugging
        print("Token CSRF:", request.POST.get('csrfmiddlewaretoken'))
        print("O formulário é válido?", form.is_valid())
        print("Erros de validação:", form.errors)
        
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva o produto no banco de dados
            form.save()
            
            # Exibe uma mensagem de sucesso para o usuário
            messages.success(request, 'Produto cadastrado com sucesso.')
            
            # Redireciona para a lista de produtos após o cadastro bem-sucedido
            return redirect('listar_produtos')

    # Renderiza a página de cadastro, passando o formulário como contexto
    return render(request, 'cadastroProduto.html', {'form': form})



# mostra todos os produtos no banco
@login_required
def listar_todos_produtos(request):
    # Obtém todos os produtos do banco de dados
    produtos = Produto.objects.all()

    # Renderiza a página 'estoque.html' passando a lista de produtos como contexto
    return render(request, 'estoque.html', {'produtos': produtos})



# edita os produtos
def editar_produto(request, produto_id):
    # Obtém o produto existente ou retorna uma página 404 se não for encontrado
    produto = get_object_or_404(Produto, id=produto_id)

    # Verifica se a requisição é do tipo POST (envio do formulário)
    if request.method == 'POST':
        # Preenche o formulário com os dados do POST e a instância do produto existente
        form = ProdutoForm(request.POST, instance=produto)
        
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva as alterações no produto no banco de dados
            form.save()
            
            # Redireciona para a lista de produtos após a edição bem-sucedida
            return redirect('listar_todos_produtos')  # Substitua pelo nome da sua URL de listagem de produtos

    # Se a requisição não é do tipo POST, exibe o formulário preenchido com os dados atuais do produto
    else:
        form = ProdutoForm(instance=produto)

    # Renderiza a página 'editar_produto.html' passando o formulário como contexto
    return render(request, 'editar_produto.html', {'form': form})



# exclui os produtos
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_todos_produtos')  # Substitua pelo nome da sua URL de listagem de produtos

    return render(request, 'excluir_produto.html', {'produto': produto})



# loja
def listar_produtos(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.all()

    if query:
        # Filtramos os produtos com base no termo de busca
        produtos = produtos.filter(
            Q(nome_produto__icontains=query) | Q(descricao_produto__icontains=query)
        )

    # Verifique se há uma solicitação de adição ao carrinho
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = 1  # ou a quantidade desejada, se aplicável

        # Recupere ou crie uma instância do carrinho para o usuário atual
        carrinho = Carrinho(request)

        # Adicione o produto ao carrinho
        carrinho.adicionar(produto_id, quantidade)

        # Redirecione de volta à página de produtos após a adição ao carrinho
        return redirect('listar_produtos')

    return render(request, 'loja.html', {'produtos': produtos, 'query': query})



def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})



# mostra os produtos no carrinho
def telaCarrinho(request):
    carrinho = Carrinho(request)
    itens = carrinho.listar_itens()
    total = carrinho.calcular_total()

    return render(request, 'carrinho.html', {'itens': itens, 'total': total})



# funcionalidades do carrinho
def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    carrinho = Carrinho(request)
    carrinho.adicionar(produto)

    return redirect('telaCarrinho')



class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho', {})
        self.carrinho = carrinho



    def adicionar(self, produto):
        produto_id = str(produto.id)
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'quantidade': 1}
        else:
            self.carrinho[produto_id]['quantidade'] += 1

        self.salvar_carrinho()



    def salvar_carrinho(self):
        self.session['carrinho'] = self.carrinho
        self.session.modified = True



    def listar_itens(self):
        items = []
        for produto_id, item in self.carrinho.items():
            produto = Produto.objects.get(id=produto_id)
            items.append({'produto': produto, 'quantidade': item['quantidade']})
        return items



    def calcular_total(self):
        total = 0
        for produto_id, item in self.carrinho.items():
            produto = Produto.objects.get(id=produto_id)
            total += produto.preco_produto * item['quantidade']
        return total
    


    def remover(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar_carrinho()



    def limpar_carrinho(self):
        self.session['carrinho'] = {}
        self.session.modified = True
    


def remover_item_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.remover(produto_id)
    return redirect('telaCarrinho')



@login_required
def tela_pagamento(request):
    carrinho = Carrinho(request)
    itens = carrinho.listar_itens()
    total = carrinho.calcular_total()

    return render(request, 'pagamento.html', {'itens': itens, 'total': total})



@login_required
def finalizar_Pagamento(request):
    carrinho = Carrinho(request)
    carrinho.limpar_carrinho()

    return render(request, 'agradecimento.html')