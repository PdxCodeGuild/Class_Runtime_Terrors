# Generated by Django 3.1.6 on 2021-02-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210217_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]