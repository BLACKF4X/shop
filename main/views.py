from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Category


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'M&B - Главная'
        context['content'] = "Магазин Маши и Медведя"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'M&B - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "ИВТ-31Д (Уже 41-Д) представляет свою версию магазина как замену 1С.\nРабота явно " \
                                  "заслуживает одобрения со стороны кафедры. "
        return context
