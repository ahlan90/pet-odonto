from _ast import arg

from django.urls import reverse
from rest_framework import serializers

from cadastros.models import *
from core.extras import Anchor


class SelecaoClienteSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = (
            'nome', 'cpf', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(url=reverse('paciente-selecao', kwargs={'pk': obj.id}), classes='btn btn-primary btn-sm', text='Selecionar')
        return str(instance)


class SelecaoPacienteSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Paciente
        fields = (
            'nome', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(url=reverse('consulta-add', kwargs={'pk': obj.id}), classes='btn btn-primary btn-sm', text='Selecionar')
        return str(instance)
