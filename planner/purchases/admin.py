from django.contrib import admin

from .forms import PostForm
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "url_name", "get_total_amount"]
    sortable_by = ("id", )

    # относительный URL-адрес
    def url_name(self, obj: Category):
        return obj.slug


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ["name", "create_dt", "amount", "category"]
    date_hierarchy = "create_dt"
    sortable_by = "category"
