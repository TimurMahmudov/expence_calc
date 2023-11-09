from django.shortcuts import render
from django.views import generic
from django.db import models

from .models import Category, Post


class GeneralInfoView(generic.ListView):
    """
    Все расходы за период
    """
    template_name = "index.html"

    def get_queryset(self):
        return Category.objects.prefetch_related("posts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = self.get_queryset()
        return context


class CategoryInfoView(generic.ListView):
    """
    Информация о расходах по выбранной категории
    """
    pass
