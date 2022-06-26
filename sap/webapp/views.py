from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    return render(request, 'bienvenido.html')


def despedida(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Email: contacto@mail.com, Tel. 5544332211')