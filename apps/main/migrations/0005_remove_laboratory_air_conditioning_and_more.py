# Generated by Django 5.0 on 2023-12-20 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_recommendation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratory',
            name='air_conditioning',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='security_camera',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('in progress', 'En progreso'), ('completed', 'Completada')], default='pending', max_length=20),
        ),
        migrations.CreateModel(
            name='Air_Conditioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
                ('voltage', models.IntegerField(verbose_name='Voltaje')),
                ('capacity', models.IntegerField(verbose_name='Capacidad')),
                ('device_type', models.CharField(max_length=50, verbose_name='Tipo')),
                ('potency', models.IntegerField(verbose_name='Potencia')),
                ('consumption', models.IntegerField(verbose_name='Consumo')),
                ('lab_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.laboratory', verbose_name='Laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Regulator_voltage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
                ('capacity', models.IntegerField(verbose_name='Capacidad')),
                ('dimensions', models.CharField(max_length=50, verbose_name='Dimensiones')),
                ('weight', models.CharField(max_length=50, verbose_name='Peso')),
                ('device_type', models.CharField(max_length=50, verbose_name='Tipo')),
                ('input_voltage', models.IntegerField(verbose_name='Voltaje de entrada')),
                ('output_voltage', models.IntegerField(verbose_name='Voltaje de salida')),
                ('output_current', models.IntegerField(verbose_name='Corriente de salida')),
                ('number_plugs', models.IntegerField(verbose_name='Número de enchufes')),
                ('lab_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.laboratory', verbose_name='Laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Security_camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('model', models.CharField(max_length=50, verbose_name='Modelo')),
                ('sensor', models.CharField(max_length=50, verbose_name='Sensor')),
                ('resolution', models.CharField(max_length=50, verbose_name='Resolución')),
                ('lens', models.CharField(max_length=50, verbose_name='Lente')),
                ('dimensions', models.CharField(max_length=50, verbose_name='Dimensiones')),
                ('lab_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.laboratory', verbose_name='Laboratorio')),
            ],
        ),
    ]
