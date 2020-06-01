from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.base import ContextMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet

from cadastros.forms import ClienteForm, PacienteForm
from cadastros.models import Cliente, Paciente, Consulta
from consulta.forms import ConsultaForm
from consulta.serializers import SelecaoClienteSerializer, SelecaoPacienteSerializer


class ConsultaView(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Consulta'
        return context


class ClienteConsultaSelecao(CreateView, ConsultaView):

    form_class = ClienteForm
    template_name = 'consulta/cliente_selecao.html'

    def get_success_url(self):
        return reverse('paciente-selecao', args=(self.object.id,))



class SelecaoClienteConsultaViewSet(ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = SelecaoClienteSerializer



class PacienteConsultaSelecao(CreateView, ConsultaView):

    form_class = PacienteForm
    template_name = 'consulta/paciente_selecao.html'

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get('pk')
        initial['cliente'] = Cliente.objects.get(pk=pk)
        return initial

    def get_success_url(self):
        return reverse('consulta-add', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_cliente = self.kwargs.get('pk')
        context['cadastros'] = Paciente.objects.filter(cliente=pk_cliente).count() > 0
        context['cliente_id'] = pk_cliente
        return context



class SelecaoPacienteConsultaViewSet(ViewSet):

    queryset = Paciente.objects.all()

    def list(self, request):

        cliente_id = request.query_params.get('cliente')
        queryset = Paciente.objects.filter(cliente=cliente_id)
        serializer = SelecaoPacienteSerializer(queryset, many=True)

        return Response(serializer.data)



class ConsultaCreate(CreateView):

    form_class = ConsultaForm
    template_name = 'consulta/consulta_form.html'
    success_url = '/consulta'

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get('pk')
        initial['paciente'] = Paciente.objects.get(pk=pk)
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Consulta'
        return context


