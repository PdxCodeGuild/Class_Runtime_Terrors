# Generated by Django 3.1.5 on 2021-01-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_auto_20210122_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cbd',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='thc',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='variety',
            name='name',
            field=models.CharField(choices=[('Indica', 'Indica'), ('Sativa', 'Sativa'), ('Hybrid', 'Hybrid')], default='Hybrid', max_length=6),
        ),
    ]
