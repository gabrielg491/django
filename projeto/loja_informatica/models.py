from django.db import models

# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveSmallIntegerField()

    def __str__(self) :
        return self.nome