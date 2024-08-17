from django.shortcuts import render
from goods.models import Product

def catalog(request):

    goods = Product.objects.all()

    context = {
        "title": "M&B - Каталог",
        "goods": goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
