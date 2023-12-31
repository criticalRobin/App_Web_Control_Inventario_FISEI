# Generated by Django 5.0 on 2023-12-09 20:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='responsible_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cpu',
            name='computer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.computer'),
        ),
        migrations.AddField(
            model_name='disk',
            name='cpu_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cpu'),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='responsible_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='computer',
            name='lab_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectors', to='main.laboratory'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='computer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.computer'),
        ),
        migrations.AddField(
            model_name='processor',
            name='cpu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cpu'),
        ),
        migrations.AddField(
            model_name='projector',
            name='lab_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.laboratory'),
        ),
        migrations.AddField(
            model_name='ram',
            name='cpu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cpu'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='computer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.computer'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='recommendation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recommendation'),
        ),
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
