from dal import autocomplete
from django.forms import ModelForm, TextInput, URLField, Form
from s3direct.widgets import S3DirectWidget

from cadastros.models import Cirurgia


class CirurgiaForm(autocomplete.FutureModelForm):

    class Meta:
        model = Cirurgia
        fields = '__all__'
        widgets = {
            'data': TextInput(attrs={'type': 'date'}),
            'local': autocomplete.ModelSelect2(
                'clinica-autocomplete'
            ),
            'veterinario_anestesista': autocomplete.ModelSelect2(
                'veterinario-autocomplete'
            ),
            'alteracoes_ondotologicas': autocomplete.ModelSelect2Multiple(
                'alteracao-odontologica-autocomplete'
            )
        }
        labels = {
            'alteracoes_ondotologicas': 'Alterações Odontológicas',
            'veterinario_anestesista': 'Veterinário anestesista'
        }


class S3DirectUploadForm(Form):
    images = URLField(widget=S3DirectWidget(dest='arquivos_cirurgia'))
