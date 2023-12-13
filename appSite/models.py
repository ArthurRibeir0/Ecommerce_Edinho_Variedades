from django.utils import timezone
from django.db import models

# produto
class Produto(models.Model):
    nome_produto = models.CharField(max_length=255, default='Produto Padrão')
    descricao_produto = models.TextField()
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_produto = models.PositiveIntegerField()
    imagem_produto = models.ImageField(upload_to='imagens_produtos/', blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)  # Adicione esta linha para a data de criação

    def __str__(self):
        return self.nome_produto
