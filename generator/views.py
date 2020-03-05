from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html', {'password': 'jhlasl324'})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    lenght = int(request.GET.get('length'))
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html', {})
