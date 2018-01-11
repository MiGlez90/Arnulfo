# Generated by Django 2.0.1 on 2018-01-11 23:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=140)),
                ('uprice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('units', models.PositiveIntegerField(default=1)),
                ('kg_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('payment', models.CharField(choices=[('TC', 'Tarjeta Credito'), ('Efectivo', 'Efectivo'), ('TD', 'Tarjeta Debito')], max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provid', to='egresos.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('weigth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('animal_ref', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='egresos.Purchase')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='egresos.Product')),
            ],
        ),
    ]
