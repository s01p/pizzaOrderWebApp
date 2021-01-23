# Generated by Django 2.0.13 on 2019-06-27 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_auto_20190627_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='dinnerPlatters',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.DinnerPlatters'),
        ),
        migrations.AddField(
            model_name='item',
            name='pasta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.Pasta'),
        ),
        migrations.AddField(
            model_name='item',
            name='regularPizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.RegularPizza'),
        ),
        migrations.AddField(
            model_name='item',
            name='salads',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.Salads'),
        ),
        migrations.AddField(
            model_name='item',
            name='sicilianPizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.SicilianPizza'),
        ),
        migrations.AddField(
            model_name='item',
            name='subs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.Subs'),
        ),
    ]