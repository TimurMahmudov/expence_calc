from django.db import models


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

    # Вытаскиваем общую сумму продуктов по данной категорииы
    def get_total_amount(self):
        object = self
        if not object.posts.exists():
            return 0
        object = object.posts.aggregate(total_amount=models.Sum("amount"))
        return round(object["total_amount"], 2)


class Post(models.Model):
    """Продукты"""
    name = models.CharField(max_length=90,
                            verbose_name="Название товара")
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 to_field="slug",
                                 related_name="posts",
                                 verbose_name="Категория")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена")
    quant = models.DecimalField(max_digits=6,
                                decimal_places=3,
                                verbose_name="Масса/Кол-во")
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 verbose_name="Сумма")
    create_dt = models.DateField(auto_now_add=True,
                                 verbose_name="Дата покупки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("category", "name",)
        verbose_name = "Наименование покупки"
        verbose_name_plural = "Покупки"
