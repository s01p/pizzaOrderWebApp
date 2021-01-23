# Generated by Django 2.0.13 on 2019-06-28 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0008_auto_20190628_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='product_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='product_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='shoppingCart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.ShoppingCart'),
        ),
        migrations.AlterField(
            model_name='regularpizza',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='regularpizza',
            name='price_large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='regularpizza',
            name='price_small',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='regularpizza',
            name='small',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='price_large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='price_small',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='small',
            field=models.FloatField(),
        ),
    ]