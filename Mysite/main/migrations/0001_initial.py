# Generated by Django 4.1.7 on 2023-03-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=50, verbose_name='Carusel head')),
                ('text', models.CharField(max_length=50, verbose_name='Carusel text')),
                ('img_bg', models.ImageField(upload_to='carusel_img_bg', verbose_name='Carusel img_bg')),
                ('img', models.ImageField(upload_to='carusel_img_bg', verbose_name='Carusel img')),
            ],
        ),
    ]
