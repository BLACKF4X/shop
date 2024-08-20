from django.shortcuts import render, redirect
from carts.models import Cart
from goods.models import Product

def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user, product=product)
            cart.quantity += 1
            cart.save()
        except Cart.DoesNotExist:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
