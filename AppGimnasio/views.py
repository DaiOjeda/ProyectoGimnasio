
from django.shortcuts import render, redirect
from datetime import datetime
from AppGimnasio.models import Cliente #Actividad


def inicio(request):
    return render(request, 'index.html')

def cliente(request):
    cliente1 = Cliente(nombre="Cristian", dni=24682468)
    cliente1.save()#hacer un if de si el dni existe, dar msj de error e ingresar otro
    contexto = {
        'cliente': cliente1
    }
    return redirect(request, 'AppGimnasio/cliente.html' , contexto)#se cambio redirect por render


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