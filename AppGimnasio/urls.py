from django.urls import path
from AppGimnasio.views import *

urlpatterns = [
    path('', inicio, name='AppGimnasioInicio'),
    path('cliente/', cliente, name='AppGimnasioCliente'),
  #  path('actividad/', actividad, name='AppGimnasioActividad'),
    path('cliente_formulario/', cliente_formulario, name = 'AppGimnasioClienteFormulario')

]