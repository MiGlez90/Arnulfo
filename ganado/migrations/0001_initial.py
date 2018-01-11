# Generated by Django 2.0.1 on 2018-01-11 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arete_siniga', models.CharField(max_length=30)),
                ('arete_rancho', models.CharField(max_length=30)),
                ('fecha_entrada', models.DateTimeField(db_index=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('peso_entrada', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('costo_kilo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('raza', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('comentarios', models.TextField()),
                ('owner', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False)),
                ('costo_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fierro_original', models.ImageField(upload_to='fierrosO/')),
                ('fierro_nuevo', models.ImageField(upload_to='fierrosN/')),
                ('ref_factura_original', models.CharField(max_length=100)),
                ('numero_semana', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('ano', models.PositiveIntegerField(blank=True, default=2010, null=True)),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=100, null=True)),
                ('cuarto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_generacion', models.DateTimeField(db_index=True)),
                ('no_corral', models.PositiveIntegerField(default=0)),
                ('comentarios', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('numero_semana', models.PositiveIntegerField(default=0)),
                ('ano', models.PositiveIntegerField(default=2010)),
                ('numero_serial', models.CharField(max_length=100)),
                ('mes', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=100)),
                ('cuarto', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GastoAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('tipo', models.CharField(blank=True, choices=[('Alimento', 'Alimento'), ('Vacuna', 'Vacuna')], max_length=100, null=True)),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aliments', to='ganado.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('status', models.BooleanField(default=False)),
                ('corral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='ganado.Corral')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='lote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='ganado.Lote'),
        ),
    ]
