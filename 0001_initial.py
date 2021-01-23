# Generated by Django 2.0.13 on 2019-06-08 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegularPizzaSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('small', models.FloatField()),
                ('large', models.FloatField()),
                ('regularpizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.RegularPizza')),
            ],
        ),
    ]
