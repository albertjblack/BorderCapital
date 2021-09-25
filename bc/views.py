from django.views import generic
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'