from django.shortcuts import render, redirect
from datetime import datetime
from AppGimnasio.models import Cliente


def inicio(request):
    return render(request, 'index.html')

def cliente(request):
    cliente1 = Cliente(nombre="cliente", dni=00000000)
    cliente1.save()#hacer un if de si el dni existe, dar msj de error e ingresar otro
    contexto = {
        'cliente': cliente1
    }
    return redirect(request, 'AppGimnasio/cliente.html' , contexto)#se cambio redirect por render

