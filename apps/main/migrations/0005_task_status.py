# Generated by Django 5.0 on 2023-12-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_recommendation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('in progress', 'En progreso'), ('completed', 'Completada')], default='pending', max_length=20),
        ),
    ]
