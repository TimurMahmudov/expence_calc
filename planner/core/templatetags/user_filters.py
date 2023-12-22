from django.shortcuts import get_object_or_404
from django import template

from purchases.models import Category

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.inclusion_tag("include/menu_categories.html")
def enclusion_menu(slug):
    content = {
        "cats": [
            cat for cat in Category.objects.all() if cat.posts.exists()
        ],
        "select_cat": Category.objects.get(slug=slug)
    }
    return content
