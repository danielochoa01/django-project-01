from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.

class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'

    form_class = NewDepartamentoForm

    success_url = '.'

    def form_valid(self, form):

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        departamento = form.cleaned_data['departamento']
        short_name = form.cleaned_data['short_name']

        departamento_object = Departamento(
            name=departamento,
            short_name=short_name
        )
        departamento_object.save()

        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            department=departamento_object
        )

        return super(NewDepartamentoView, self).form_valid(form)
