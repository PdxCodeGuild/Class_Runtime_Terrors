# Generated by Django 3.0 on 2021-02-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0002_auto_20210217_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='restroom',
            name='latitude',
            field=models.DecimalField(decimal_places=16, default=1, max_digits=22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restroom',
            name='longitude',
            field=models.DecimalField(decimal_places=16, default=1, max_digits=22),
            preserve_default=False,
        ),
    ]
