from django.db import models


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=100, null=False)
    CPF = models.CharField(max_length=100, null=False)
    mensagem = models.TextField(max_length=455)
    data_criacao = models.DateTimeField(auto_now_add=True)
    


# Create your models here.
