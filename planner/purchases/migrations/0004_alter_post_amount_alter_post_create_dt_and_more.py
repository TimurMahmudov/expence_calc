# Generated by Django 4.2.6 on 2023-11-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_alter_post_amount_alter_post_price_alter_post_quant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='Конечная стоимость', max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_dt',
            field=models.DateField(auto_now_add=True, help_text='Дата покупки', verbose_name='Дата покупки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(help_text='Наименование продукта', max_length=90, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Цена', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quant',
            field=models.DecimalField(decimal_places=3, help_text='Масса/Кол-во', max_digits=6, verbose_name='Масса/Кол-во'),
        ),
    ]
