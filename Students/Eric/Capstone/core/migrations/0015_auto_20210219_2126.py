# Generated by Django 3.1.6 on 2021-02-20 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_ask_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ask',
            old_name='number',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ask',
            old_name='title',
            new_name='request',
        ),
    ]