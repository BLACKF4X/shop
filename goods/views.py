from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from goods.models import Product
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)  # Changed this line

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "M&B - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)
