from dal import autocomplete
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin
from rest_framework import viewsets

from cadastros.forms import ClienteForm, PacienteForm
from cadastros.models import *
from cadastros.serializers import ClienteSerializer, PacienteSerializer, ClinicaSerializer, \
    AlteracaoOdontologicaSerializer, CirurgiaSerializer, VeterinarioSerializer, ConsultaSerializer, RacaSerializer
from consulta.forms import ConsultaForm

"""
CRUD ALTERACOES ODONTOLOGICAS
"""
class AlteracaoOdontologicaList(LoginRequiredMixin, ListView):
    model = AlteracaoOdontologica

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Alterações Odontologicas'
        return context


class AlteracaoOdontologicaCreate(SuccessMessageMixin, CreateView):
    success_url = '/alteracao-odontologica'
    model = AlteracaoOdontologica
    fields = '__all__'
    success_message = 'Alteração Odontológica incluida com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Alteração Odontológica'
        return context

class AlteracaoOdontologicaUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/alteracao-odontologica'
    model = AlteracaoOdontologica
    fields = '__all__'
    success_message = 'Alteração Odontológica editada com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Alteração Odontológica'
        return context

class AlteracaoOdontologicaDelete(DeleteView):
    model = AlteracaoOdontologica
    success_url = reverse_lazy('alteracao-odontologica-list')

class AlteracaoOdontologicaViewSet(viewsets.ModelViewSet):
    queryset = AlteracaoOdontologica.objects.all()
    serializer_class = AlteracaoOdontologicaSerializer


"""
CRUD CIRURGIA
"""
class CirurgiaList(ListView):
    model = Cirurgia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cirurgias'
        return context



class CirurgiaCreate(SuccessMessageMixin, CreateView):
    success_url = '/cirurgia'
    model = Cirurgia
    fields = '__all__'
    success_message = 'Cirurgia incluida com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Cirurgia'
        return context


class CirurgiaUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/cirurgia'
    model = Cirurgia
    fields = '__all__'
    success_message = 'Cirurgia editada com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cirurgia'
        return context


class CirurgiaDelete(DeleteView):
    model = Cirurgia
    success_url = reverse_lazy('cirurgia-list')


class CirurgiaViewSet(viewsets.ModelViewSet):
    queryset = Cirurgia.objects.all()
    serializer_class = CirurgiaSerializer


"""
CRUD CLIENTE
"""
class ClienteList(ListView):
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Clientes'
        context['btn_add'] = True
        return context


class ClienteCreate(SuccessMessageMixin, CreateView):
    success_url = '/cliente'
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente incluido com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Cliente'
        return context


class ClienteUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/cliente'
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente editado com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        return context


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



"""
CRUD CLINICA
"""
class ClinicaList(ListView):
    model = Clinica

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Clínicas'
        return context


class ClinicaCreate(SuccessMessageMixin, CreateView):
    success_url = '/clinica'
    model = Clinica
    fields = '__all__'
    success_message = 'Clinica criada com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Clínica'
        return context



class ClinicaUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/clinica'
    model = Clinica
    fields = '__all__'
    success_message = 'Clinica atualizada com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualizar Clínica'
        return context

class ClinicaDelete(SuccessMessageMixin, DeleteView):
    model = Clinica
    success_url = reverse_lazy('clinica-list')
    success_message = 'Clínica removida com sucesso!!!'

class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer


class ClinicaAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):

        qs = Clinica.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

"""
CRUD CONSULTA
"""
class ConsultaList(ListView):
    model = Consulta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Consultas'
        return context

class ConsultaCreate(SuccessMessageMixin, CreateView):
    success_url = '/consulta'
    model = Consulta
    form_class = ConsultaForm
    success_message = 'Consulta incluida com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Consulta'
        return context

class ConsultaUpdate(SuccessMessageMixin, UpdateView):
    template_name = "consulta/consulta_form.html"
    success_url = '/consulta'
    model = Consulta
    fields = '__all__'
    success_message = 'Consulta incluida com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Consulta'
        return context

class ConsultaDelete(DeleteView):
    model = Consulta
    success_url = reverse_lazy('consulta-list')


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer



"""
CRUD PACIENTE
"""

class PacienteList(ListView):

    model = Paciente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Pacientes'
        return context

class PacienteCreate(SuccessMessageMixin, CreateView):
    success_url = '/paciente'
    model = Paciente
    form_class = PacienteForm
    success_message = 'Paciente incluido com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Paciente'
        return context


class PacienteUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/paciente'
    model = Paciente
    fields = '__all__'
    success_message = 'Paciente incluido com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Paciente'
        return context


class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente-list')


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer



"""
CRUD VETERINARIO
"""
class VeterinarioList(ListView):
    model = Veterinario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Veterinários'
        return context


class VeterinarioCreate(SuccessMessageMixin, CreateView):
    success_url = '/veterinario'
    model = Veterinario
    fields = '__all__'
    success_message = 'Veterinário incluido com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Veterinário'
        return context

class VeterinarioUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/veterinario'
    model = Veterinario
    fields = '__all__'
    success_message = 'Veterinário editado com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Veterinário'
        return context


class VeterinarioDelete(DeleteView):
    model = Veterinario
    success_url = reverse_lazy('veterinario-list')


class AnestesistaViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

"""
CRUD EXAME
"""
class ExameList(TemplateView):

    template_name = "cadastros/exame.html"



"""
CRUD FOTO
"""
class FotoList(TemplateView):

    template_name = "cadastros/foto.html"




"""
CRUD RACA
"""
class RacaList(ListView):
    model = Raca

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Raças'
        return context


class RacaCreate(SuccessMessageMixin, CreateView):
    success_url = '/raca'
    model = Raca
    success_message = 'Raça incluida com sucesso!!!'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Raça'
        return context


class RacaUpdate(SuccessMessageMixin, UpdateView):
    success_url = '/raca'
    model = Raca
    fields = '__all__'
    success_message = 'Raça editada com sucesso!!!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Raça'
        return context


class RacaDelete(DeleteView):
    model = Raca
    success_url = reverse_lazy('raca-list')


class RacaViewSet(viewsets.ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer