# Generated by Django 4.1.7 on 2023-03-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carusel',
            name='text',
            field=models.TextField(verbose_name='Carusel text'),
        ),
    ]
