# Generated by Django 3.1.4 on 2021-01-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageloader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='header_image',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y'),
        ),
    ]