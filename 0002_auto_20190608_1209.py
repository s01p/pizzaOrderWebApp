# Generated by Django 2.0.13 on 2019-06-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularpizzasize',
            name='regularpizza',
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='large',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='price_large',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='price_small',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='small',
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name='RegularPizzaSize',
        ),
    ]
