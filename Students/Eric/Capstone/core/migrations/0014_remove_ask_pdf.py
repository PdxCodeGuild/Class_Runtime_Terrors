# Generated by Django 3.1.6 on 2021-02-20 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_ask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ask',
            name='pdf',
        ),
    ]