import re
from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    contraGenerada = ''

    #Se guarda en la variable "longitud" el parametro recibido mediante el metodo GET, que indica la seleccion del select de nombre lenght   
    longitud = int(request.GET.get('lenght'))

    # verificar si checkbox "uppercase" para incluir caracteres en mayúsculas, esta seleccionado | Sí lo esta, agrega caracteres en mayúscula a la lista "caracteres"
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # verificar si checkbox "special" para incluir caracteres especiales, esta seleccionado | Sí lo esta, agrega caracteres especiales a la lista "caracteres"
    if request.GET.get('special'):
        caracteres.extend(list("'!#$%&*/\+_-?@"))

    # verificar si checkbox "numbers" para incluir caracteres numericos, esta seleccionado | Sí lo esta, agrega números a la lista "caracteres"
    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))

    # Ciclo de rango del valor de la variable longitud, que se obtiene de lo seleccionado en el select lenght, para insertar en la variable contraGenerada, caracteres randoms inclidos en la lista caracteres
    for x in range(longitud):
        contraGenerada += random.choice(caracteres)

    return render(request, 'generator/password.html', {'contra': contraGenerada})