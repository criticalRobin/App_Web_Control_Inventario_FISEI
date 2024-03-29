# Generated by Django 4.2.7 on 2024-01-07 20:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_computeritem_labitem_remove_cpu_computer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='chair_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Número de sillas'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='floor_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='Número de piso'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='table_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='Número de mesas'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='user_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
