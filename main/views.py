from django.http import HttpResponse
from django.shortcuts import render


def index (reqest):
    context: any = {
        'title': 'Home',
        'content': 'Главная страница магазина - Internet Store'
    }

    return render(reqest, 'main/index.html', context)

def about (reqest):
    return HttpResponse('About page')