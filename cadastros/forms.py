from dal import autocomplete
from django.forms import ModelForm, TextInput, HiddenInput

from cadastros.models import Cliente, Paciente, Clinica


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        exclude = ['user']


class PacienteForm(autocomplete.FutureModelForm):

      class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'data_nascimento': TextInput(attrs={'type': 'date'}),
            'cliente': autocomplete.ModelSelect2(
                'cliente-autocomplete'
            ),
            'raca': autocomplete.ModelSelect2(
                'teste_raca_autocomplete'
            )
        }
