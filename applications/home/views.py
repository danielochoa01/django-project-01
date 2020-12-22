from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'lista_numeros'
    queryset = [str(i) for i in range(0, 40, 10)]


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = 'home/add.html'

    form_class = PruebaForm
    success_url = '/'