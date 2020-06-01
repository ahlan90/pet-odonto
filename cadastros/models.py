from datetime import datetime
from tabnanny import verbose

from django.contrib.auth.models import User
from django.db import models
from s3direct.fields import S3DirectField


class Cliente(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=500)
    telefone = models.CharField(max_length=500)
    cpf = models.CharField(max_length=15, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Veterinario(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class Raca(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Paciente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField("Nome do Pet", max_length=200)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    peso = models.DecimalField(max_digits=12, decimal_places=3)
    veterinario_encaminhamento = models.CharField("Veterinário do encaminhamento", max_length=200)

    def __str__(self):
        return self.nome + " - " + self.cliente.nome



class Clinica(models.Model):
    name = models.CharField("Nome", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class AlteracaoOdontologica(models.Model):

    name = models.CharField("Nome", max_length=500)

    def __str__(self):
        return self.name


class Consulta(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    local = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now())
    anamnse = models.TextField(max_length=10000)


class Cirurgia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    local = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    veterinario_anestesista = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    alteracoes_ondotologicas = models.ManyToManyField(AlteracaoOdontologica)
    prontuario_cirurgico = models.TextField("Prontuário cirúrgico", max_length=10000)


class ArquivosCirurgia(models.Model):
    cirurgia = models.ForeignKey(Cirurgia, on_delete=models.CASCADE)
    arquivo = S3DirectField(dest='arquivos_cirurgia')
