# Generated by Django 4.0.2 on 2022-02-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0001_initial'),
        ('Personas', '0003_alter_funcionario_identificacion_alter_proveedor_nit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.elemento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personas.funcionario')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
    ]
