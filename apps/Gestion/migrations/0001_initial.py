# Generated by Django 4.0.3 on 2022-03-26 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personas', '0001_initial'),
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deBaja', models.BooleanField(default=False)),
                ('descripcion', models.TextField(max_length=20000000000)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, max_length=20000000000, null=True)),
                ('enProceso', models.BooleanField(default=False)),
                ('finalizado', models.BooleanField(default=False)),
                ('irreparable', models.BooleanField(blank=True, default=False, null=True)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('timestampsF', models.DateTimeField(blank=True, null=True)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.elemento')),
            ],
            options={
                'verbose_name': 'Mantenimiento',
                'verbose_name_plural': 'Mantenimientos',
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.elemento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personas.funcionario')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
    ]
