# Generated by Django 2.0.13 on 2019-07-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_shoppingcart_checked_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='date_of_checked_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
