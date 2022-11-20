from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница!!',
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')