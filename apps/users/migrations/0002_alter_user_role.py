# Generated by Django 5.0 on 2023-12-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Student', 'Estudiante'), ('Technical', 'Técnico')], default='Student', max_length=10),
        ),
    ]