from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from cadastros.forms import ClienteForm, PacienteForm
from cadastros.models import Cliente, Paciente, Cirurgia, ArquivosCirurgia
from cirurgia.forms import CirurgiaForm, S3DirectUploadForm
from cirurgia.serializers import CirurgiaSelecaoClienteSerializer, CirurgiaSelecaoPacienteSerializer


class ClienteCirurgiaSelecao(CreateView):

    form_class = ClienteForm
    template_name = 'cirurgia/cliente_selecao.html'

    def get_success_url(self):
        return reverse('paciente-selecao', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Cirurgia'
        return context



class SelecaoClienteCirurgiaViewSet(ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = CirurgiaSelecaoClienteSerializer



class PacienteCirurgiaSelecao(CreateView):

    form_class = PacienteForm
    template_name = 'cirurgia/paciente_selecao.html'

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get('pk')
        initial['cliente'] = Cliente.objects.get(pk=pk)
        return initial

    def get_success_url(self):
        return reverse('cirurgia-add', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_cliente = self.kwargs.get('pk')
        context['cadastros'] = Paciente.objects.filter(cliente=pk_cliente).count() > 0
        context['cliente_id'] = pk_cliente
        return context



class SelecaoPacienteCirurgiaViewSet(ViewSet):

    queryset = Paciente.objects.all()

    def list(self, request):

        cliente_id = request.query_params.get('cliente')
        queryset = Paciente.objects.filter(cliente=cliente_id)
        serializer = CirurgiaSelecaoPacienteSerializer(queryset, many=True)

        return Response(serializer.data)



class CirurgiaCreate(CreateView):

    form_class = CirurgiaForm
    template_name = 'cirurgia/cirurgia_form.html'
    success_url = '/cirurgia'

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get('pk')
        initial['paciente'] = Paciente.objects.get(pk=pk)
        return initial


# class CirurgiaArquivos(CreateView):
#
#     form_class = S3DirectUploadForm
#     template_name = 'cirurgia/cirurgia_arquivo_form.html'
#     success_url = '/cirurgia'
#
#     # def get_initial(self):
#     #     initial = super().get_initial()
#     #     pk = self.kwargs.get('pk')
#     #     initial['cirurgia'] = Cirurgia.objects.get(pk=pk)
#     #     return initial


def cirurgia_images_new(request, cirurgia_id):
    cirurgia = get_object_or_404(Cirurgia, pk=cirurgia_id)

    form = S3DirectUploadForm()

    if request.method == 'POST':
        form = S3DirectUploadForm(request.POST)
        if form.is_valid():
            upload = ArquivosCirurgia()
            upload.cirurgia = cirurgia
            upload.images = form.cleaned_data['images']
            upload.save()

            return redirect('cirurgia-list', cirurgia_id)

    context = {
        'form': form,
        'cirurgia': cirurgia
    }

    return render(request, 'cirurgia/cirurgia_arquivo_form.html', context)
