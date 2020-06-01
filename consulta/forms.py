from dal import autocomplete
from django.forms import ModelForm, TextInput, HiddenInput, ModelChoiceField
from cadastros.models import Consulta, Clinica


class ConsultaForm(autocomplete.FutureModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'data': TextInput(attrs={'type': 'date'}),
            'local': autocomplete.ModelSelect2(
                'clinica-autocomplete'
            )
        }
