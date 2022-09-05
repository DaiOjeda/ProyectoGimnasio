from AppGimnasio.views import *

urlpatterns = [
    path('', inicio, name='AppGimnasioInicio'),
    path('cliente/', cliente, name='AppGimnasioCliente'),

]