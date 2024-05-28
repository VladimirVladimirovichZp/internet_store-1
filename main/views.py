from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: any = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: any = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о магазине, классный магазин, лучше всех и т.д.'
    } 
     
    return render(request, 'main/about.html', context)
