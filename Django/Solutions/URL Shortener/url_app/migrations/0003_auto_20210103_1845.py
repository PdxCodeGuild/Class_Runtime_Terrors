# Generated by Django 3.1.3 on 2021-01-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0002_url_shortener_shortened_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_shortener',
            name='shortened_url',
            field=models.CharField(max_length=800),
        ),
    ]
