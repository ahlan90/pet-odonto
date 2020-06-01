from rest_framework import serializers

from cadastros.models import *
from core.extras import Anchor


class ClienteSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = (
            'nome', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(url='cliente/' + str(obj.id), classes='btn btn-primary btn-sm', text='Editar')
        return str(instance)



class PacienteSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Paciente
        fields = (
            'nome', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(url='paciente/' + str(obj.id), classes='btn btn-primary btn-sm', text='Editar')
        return str(instance)


class ClinicaSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Clinica
        fields = (
            'name', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(
            url='clinica/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)


class ConsultaSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()
    paciente = serializers.SerializerMethodField()

    class Meta:
        model = Consulta
        fields = (
            'paciente', 'data', 'botoes'
        )

    def get_data(self, obj):
        return obj.data.strftime("%d/%m/%Y")

    def get_paciente(self, obj):
        return obj.paciente.nome

    def get_botoes(self, obj):
        instance = Anchor(
            url='consulta/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)

class AlteracaoOdontologicaSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = AlteracaoOdontologica
        fields = (
            'name', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(
            url='alteracao-odontologica/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)


class CirurgiaSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()
    paciente = serializers.SerializerMethodField()

    class Meta:
        model = Cirurgia
        fields = (
            'paciente', 'data', 'botoes'
        )

    def get_data(self, obj):
        return obj.data.strftime("%d/%m/%Y")

    def get_paciente(self, obj):
        return obj.paciente.nome

    def get_botoes(self, obj):
        instance = Anchor(
            url='cirurgia/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)


class VeterinarioSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Veterinario
        fields = (
            'name', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(
            url='veterinario/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)


class RacaSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Raca
        fields = (
            'name', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(
            url='raca/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)



class VeterinarioSerializer(serializers.ModelSerializer):

    botoes = serializers.SerializerMethodField()

    class Meta:
        model = Veterinario
        fields = (
            'name', 'botoes'
        )

    def get_botoes(self, obj):
        instance = Anchor(
            url='veterinario/' + str(obj.id),
            classes='btn btn-primary btn-sm',
            text="<i class='fa fa-edit'></i> Editar"
        )
        return str(instance)
