from django.shortcuts import render, redirect
from datetime import datetime
from AppGimnasio.models import Cliente


def inicio(request):
    return render(request, 'index.html')

def cliente(request):
    cliente1 = Cliente(nombre="cliente", dni=00000000)
    cliente1.save()
    contexto = {
        'cliente': cliente1
    }
    return render(request, 'AppGimnasio/cliente.html' , contexto)

