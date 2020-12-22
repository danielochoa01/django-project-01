from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm


# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    """
        Lista todos los empleados en total
    """

    template_name = 'persona/list_all.html'
    paginate_by = 4
    context_object_name = 'empleados'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        lista = Empleado.objects.filter(
            full_name__icontains = keyword
        )

        return lista


class ListaEmpleadosAdmin(ListView):
    """
        Lista todos los empleados en total
    """

    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleados(ListView):
    """
        Lista los empleados de un área específica
    """

    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shortname']
        return Empleado.objects.filter(
            department__short_name = area
        )


class ListEmpleadosByKeyword(ListView):
    """
        Lista los empleados por palabra clave
    """

    template_name = 'persona/list_by_keyword.html'
    context_object_name = 'Empleados'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        lista = Empleado.objects.filter(
            first_name = keyword
        )
        return lista


class ListHabilidadesEmpleados(ListView):
    """
        Lista los empleados por habilidades
    """

    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id = 1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'

        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # lógica de la función
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'department',
        'habilidades'
    ]

    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # lógica de la función
        return super(EmpleadoUpdateView, self).form_valid(form)    


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'

    success_url = reverse_lazy('persona_app:empleados_admin')