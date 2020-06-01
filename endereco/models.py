from django.db import models

# Create your models here.

class Endereco(models.Model):

    cep = models.CharField(max_length=12)
    cidade = models.CharField(max_length=300)
    bairro = models.CharField(max_length=200)
    logradouro = models.CharField(max_length=500)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=300, null=True)