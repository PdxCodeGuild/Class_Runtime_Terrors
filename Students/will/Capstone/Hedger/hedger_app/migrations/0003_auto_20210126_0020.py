# Generated by Django 2.2.17 on 2021-01-26 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hedger_app', '0002_auto_20210125_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='title',
            new_name='username',
        ),
    ]