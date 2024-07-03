from django.urls import path
from mashaandbearshop.goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]
