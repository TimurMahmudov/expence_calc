from datetime import date
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=40,
                            unique=True,
                            verbose_name="Наименование")
    slug = models.SlugField(unique=True,
                            db_index=True,
                            verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def _get_current_month(self):
        return date.today().month

    # Вытаскиваем общую сумму продуктов по данной категорииы
    def get_total_amount(self):
        current_month = self._get_current_month()
        object = self
        if not object.posts.exists():
            return 0
        object = object.posts.filter(
            create_dt__month=current_month
        ).aggregate(
            total_amount=models.Sum("amount")
        )
        return round(object["total_amount"], 2)

    get_total_amount.short_description = "Общая сумма расхода"

    def get_absolute_url(self):
        return reverse("purchases:category", kwargs={"slug": self.slug})

    get_absolute_url.short_description = "URL"


class Post(models.Model):
    """Продукты"""
    name = models.CharField(max_length=90,
                            verbose_name="Название товара",
                            help_text="Введите название продукта")
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 to_field="slug",
                                 related_name="posts",
                                 verbose_name="Категория",
                                 help_text="Выберите категорию")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена",
                                help_text="Укажите цену")
    quant = models.DecimalField(max_digits=6,
                                decimal_places=3,
                                verbose_name="Масса/Кол-во",
                                help_text="Укажите массу/кол-во")
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 verbose_name="Сумма",
                                 help_text="Конечная стоимость")
    create_dt = models.DateField(auto_now_add=True,
                                 verbose_name="Дата покупки",
                                 help_text="Дата покупки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("category", "name",)
        verbose_name = "Наименование покупки"
        verbose_name_plural = "Покупки"
