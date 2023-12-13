# Em sua classe Carrinho, adicione o método adicionar
class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')

        if 'carrinho' not in request.session:
            carrinho = self.session['carrinho'] = {}

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
        # Implemente a lógica para recuperar os itens do carrinho
        pass

    # Adicione outros métodos conforme necessário