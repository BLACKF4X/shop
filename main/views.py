from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        'title': 'M&B - Главная',
        'content': "Магазин"
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'M&B - О нас',
        'content': "О нас",
        'text_on_page': "ЕБАТЬ ОКНО АХУЕННОЕ"
    }

    return render(request, 'main/about.html', context)