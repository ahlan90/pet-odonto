from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'cliente-selecao-table', SelecaoClienteConsultaViewSet)
router.register(r'paciente-selecao-table', SelecaoPacienteConsultaViewSet, basename='pacientes-table')

urlpatterns = [

    path('api/', include(router.urls)),

    path('consulta/cliente', ClienteConsultaSelecao.as_view(), name='cliente-selecao'),
    path('consulta/paciente/<int:pk>', PacienteConsultaSelecao.as_view(), name='paciente-selecao'),

    path('consulta/add/<int:pk>', ConsultaCreate.as_view(), name='consulta-add'),
]
