from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Category


def index(request):
    context = {
        'title': 'M&B - Главная',
        'content': "Магазин",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'M&B - О нас',
        'content': "О нас",
        'text_on_page': "ИВТ-31Д (Уже 41-Д) представляет свою версию магазина как замену 1С.\nРабота явно "
                        "заслуживает одобрения со стороны кафедры."
    }

    return render(request, 'main/about.html', context)

