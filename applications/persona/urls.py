from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar_todo_empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar_por_area/<shortname>/', views.ListByAreaEmpleados.as_view(), name='empleados_area'),
    path('lista_empleados_admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),    
    path('buscar_empleado/', views.ListEmpleadosByKeyword.as_view()),
    path('lista_habilidades_empleado/', views.ListHabilidadesEmpleados.as_view()),
    path('ver_empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add_empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),    
]
