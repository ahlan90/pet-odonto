from django.conf.urls import url
from django.urls import path, include
from django.views import generic
from rest_framework import routers, VERSION

from consulta.views import ConsultaCreate
from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'clinicas', ClinicaViewSet)
router.register(r'alteracoes', AlteracaoOdontologicaViewSet)
router.register(r'cirurgias', CirurgiaViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'anestesistas', AnestesistaViewSet)
router.register(r'racas', RacaViewSet)

urlpatterns = [

    path('api/', include(router.urls)),

    path('alteracao-odontologica', AlteracaoOdontologicaList.as_view(), name='alteracao-odontologica-list'),
    path('alteracao-odontologica/add/', AlteracaoOdontologicaCreate.as_view(), name='alteracao-odontologica-add'),
    path('alteracao-odontologica/<int:pk>/', AlteracaoOdontologicaUpdate.as_view(),
         name='alteracao-odontologica-update'),
    path('alteracao-odontologica/<int:pk>/delete/', AlteracaoOdontologicaDelete.as_view(),
         name='alteracao-odontologica-delete'),
    path('alteracao-odontologica-autocomplete',
         autocomplete.Select2QuerySetView.as_view(
             model=AlteracaoOdontologica,
             create_field='name'
         ),
         name='alteracao-odontologica-autocomplete'
         ),

    path('cirurgia', CirurgiaList.as_view(), name='cirurgia-list'),
    path('cirurgia/add/', CirurgiaCreate.as_view(), name='cirurgia-add'),
    path('cirurgia/<int:pk>/', CirurgiaUpdate.as_view(), name='cirurgia-update'),
    path('cirurgia/<int:pk>/delete/', CirurgiaDelete.as_view(), name='cirurgia-delete'),

    path('cliente', ClienteList.as_view(), name='cliente-lista'),
    path('cliente/add/', ClienteCreate.as_view(), name='cliente-add'),
    path('cliente/<int:pk>/', ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente/<int:pk>/delete/', ClienteDelete.as_view(), name='cliente-delete'),
    path('cliente-autocomplete',
         autocomplete.Select2QuerySetView.as_view(),
         name='cliente-autocomplete'
         ),

    path('clinica', ClinicaList.as_view(), name='clinica-list'),
    path('clinica/add/', ClinicaCreate.as_view(), name='clinica-add'),
    path('clinica/<int:pk>/', ClinicaUpdate.as_view(), name='clinica-update'),
    path('clinica/<int:pk>/delete/', ClinicaDelete.as_view(), name='clinica-delete'),
    path('clinica-autocomplete',
         autocomplete.Select2QuerySetView.as_view(
             model=Clinica,
             create_field='name'
         ),
         name='clinica-autocomplete'
         ),

    path('consulta', ConsultaList.as_view(), name='consulta-list'),
    path('consulta/add/', ConsultaCreate.as_view(), name='consulta-add'),
    path('consulta/<int:pk>/', ConsultaUpdate.as_view(), name='consulta-update'),
    path('consulta/<int:pk>/delete/', ConsultaDelete.as_view(), name='consulta-delete'),

    path('paciente', PacienteList.as_view(), name='paciente-list'),
    path('paciente/add/', PacienteCreate.as_view(), name='paciente-add'),
    path('paciente/<int:pk>/', PacienteUpdate.as_view(), name='paciente-update'),
    path('paciente/<int:pk>/delete/', PacienteDelete.as_view(), name='paciente-delete'),

    path('exame', ExameList.as_view(), name='exame-list'),

    path('foto', FotoList.as_view(), name='foto-list'),

    path('raca', RacaList.as_view(), name='raca-list'),
    path('raca/add/', RacaCreate.as_view(), name='raca-add'),
    path('raca/<int:pk>/', RacaUpdate.as_view(), name='raca-update'),
    path('raca/<int:pk>/delete/', RacaDelete.as_view(), name='raca-delete'),
    url('raca-autocomplete/$',
         autocomplete.Select2QuerySetView.as_view(
             model=Raca,
             create_field='name'
         ),
          name='teste_raca_autocomplete'
         ),

    path('veterinario', VeterinarioList.as_view(), name='veterinario-list'),
    path('veterinario/add/', VeterinarioCreate.as_view(), name='veterinario-add'),
    path('veterinario/<int:pk>/', VeterinarioUpdate.as_view(), name='veterinario-update'),
    path('veterinario/<int:pk>/delete/', VeterinarioDelete.as_view(), name='veterinario-delete'),
    path('veterinario-autocomplete',
         autocomplete.Select2QuerySetView.as_view(
             model=Veterinario,
             create_field='name'
         ),
         name='veterinario-autocomplete'
         ),
]
