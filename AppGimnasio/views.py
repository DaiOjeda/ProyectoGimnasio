
from django.shortcuts import render, redirect
from datetime import datetime
from AppGimnasio.forms import ClienteFormulario
from AppGimnasio.models import Cliente #Actividad


def inicio(request):
    return render(request, 'index.html')

def cliente(request):
    cliente1 = Cliente(nombre="Cristian", dni=24682468)
    cliente1.save()
    contexto = {
        'cliente': cliente1
    }
    return redirect(request, 'AppGimnasio/cliente.html' , contexto)#se cambio redirect por render

def cliente_formulario(request):
    if request.method == 'POST': #Se carga formulario
        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid(): #Se valida formulario
            data = mi_formulario.cleaned_data #Si es valido captura la data
            cliente1 = Cliente(nombre=data.get('nombre'), dni=data.get('dni')) #Se guarda la data
            cliente1.save()

            return redirect('AppGimnasioCliente')

        clientes = Cliente.objects.all()

        contexto = {
            'form': ClienteFormulario(),
            'clientes': clientes
        }
        return render(request, 'AppGimnasio/cliente_formulario.html', contexto)



# def actividad(request):
#     actividades = [
#         {
#             'nombre': "",
#             'fecha': "",
#             'entregado': True
#         },
#         {
#             'nombre': "",
#             'fecha': "",
#             'entregado': True
#         },
#         {
#             'nombre': "",
#             'fecha': "",
#             'entregado': True
#         },
#     ]
#     year = 2022
#     month = 10
#     day = 21
#     actividad1 = Actividad(
#         nombre= "Cristian",
#         fecha_de_entrega=datetime.date(year=year, month=month, day=day),  # date year month day
#         entregado=True
#     )
#     actividad1.save()

#     contexto = {
#         'actividad': actividad1
#     }

#     return redirect(request, 'actividad.html', contexto)





    # def entregable(request):
    # entregables = [
    #     {
    #         'nombre': "",
    #         'fecha': "",
    #         'entregado': True
    #     },
    #     {
    #         'nombre': "",
    #         'fecha': "",
    #         'entregado': True
    #     },
    #     {
    #         'nombre': "",
    #         'fecha': "",
    #         'entregado': True
    #     },
    # ]
    # year = 2000
    # month = 10
    # day = 21
    # entregable1 = Entregable(
    #     nombre="Luis",
    #     fecha_de_entrega=datetime.date(year=year, month=month, day=day),  # date year month day
    #     entregado=True
    # )
    # entregable1.save()

    # contexto = {
    #     'entregable': entregable1
    # }

    # return render(request, 'entregable.html', contexto)