from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from .models import Category, Post
from .forms import PostForm


def index(request):
    return redirect('purchases/')


class GeneralInfoView(generic.ListView):
    """
    Все расходы за период
    """
    template_name = "purchases/index.html"

    def get_queryset(self):
        cats = Category.objects.prefetch_related("posts")
        return [
            cat for cat in cats if cat.posts.exists()
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = self.get_queryset()
        return context


class CategoryInfoView(generic.ListView):
    """
    Информация о расходах по выбранной категории
    """
    template_name = "purchases/category.html"

    # Выбор категории товаров
    def get_queryset(self):
        slug_name = self.kwargs.get("slug")
        return Category.objects.prefetch_related("posts").get(slug=slug_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = self.get_queryset()
        context["slug"] = self.kwargs.get("slug")
        return context


def create_expenses(request):
    """
    Добавление новых расходов
    """
    PostFormSet = formset_factory(PostForm, extra=2, validate_min=True)
    template_name = "purchases/create_posts.html"
    if request.method == "POST":
        formset = PostFormSet(request.POST or None)
        for form in formset:
            if form.is_valid():
                form.save()
                return redirect("purchases:index")
            else:
                pass
        context = {
            "formset": PostFormSet()
        }
        return render(request, template_name, context)
    context = {
        "formset": PostFormSet()
    }
    return render(request, template_name, context)
