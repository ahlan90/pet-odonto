from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

"""
OUTRAS VIEWS
"""
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Menu'
        return context
