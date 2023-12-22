# Generated by Django 4.2.6 on 2023-12-20 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0004_alter_post_amount_alter_post_create_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='purchases.category', to_field='slug', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(help_text='Введите название продукта', max_length=90, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Укажите цену', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quant',
            field=models.DecimalField(decimal_places=3, help_text='Укажите массу/кол-во', max_digits=6, verbose_name='Масса/Кол-во'),
        ),
    ]
