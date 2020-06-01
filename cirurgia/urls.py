from django.urls import path, include
from rest_framework import routers

from . import views
from .serializers import CirurgiaSelecaoPacienteSerializer
from .views import *

router = routers.SimpleRouter()
router.register(r'cliente-selecao-table', SelecaoClienteCirurgiaViewSet)
router.register(r'paciente-selecao-table', SelecaoPacienteCirurgiaViewSet, basename='cirurgia-paciente-table')

urlpatterns = [
    path('api/cirurgia/', include(router.urls)),
    path('cirurgia/cliente', ClienteCirurgiaSelecao.as_view(), name='cirurgia-cliente-selecao'),
    path('cirurgia/paciente/<int:pk>', PacienteCirurgiaSelecao.as_view(), name='cirurgia-paciente-selecao'),
    path('cirurgia/add/<int:pk>', CirurgiaCreate.as_view(), name='cirurgia-add'),
    path('cirurgia/arquivo/<int:cirurgia_id>', views.cirurgia_images_new, name='cirurgia-arquivo-add'),
]
