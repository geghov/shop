# Generated by Django 4.1.7 on 2023-03-29 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], default=1, max_length=30, verbose_name='condition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cotegory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='l1_prod', to='main.categoryl1'),
            preserve_default=False,
        ),
    ]
