# Generated by Django 2.0.1 on 2018-01-24 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0004_auto_20180124_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fierro_nuevo',
            field=models.ImageField(blank=True, null=True, upload_to='fierrosN/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='fierro_original',
            field=models.ImageField(blank=True, null=True, upload_to='fierrosO/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='lote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='ganado.Lote'),
        ),
        migrations.AlterField(
            model_name='gastoanimal',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aliments', to='ganado.Animal'),
        ),
    ]
