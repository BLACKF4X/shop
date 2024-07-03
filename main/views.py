from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Category


def index(request):

    category = Category.objects.all()

    context = {
        'title': 'M&B - Главная',
        'content': "Магазин",
        'categories': category
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'M&B - О нас',
        'content': "О нас",
        'text_on_page': "ЕБАТЬ ОКНО АХУЕННОЕ"
    }

    return render(request, 'main/about.html', context)