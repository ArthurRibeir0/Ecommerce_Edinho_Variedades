from django import forms
from .models import Produto
from django.contrib.auth import get_user_model




# # formulario de cadastro de usuario
# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['nome_usuario', 'email_usuario', 'senha_usuario']



class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'descricao_produto', 'preco_produto', 'quantidade_produto', 'imagem_produto']

        UserModel = get_user_model()

