# Generated by Django 3.1.5 on 2021-01-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL_alter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=800)),
                ('short_url', models.CharField(max_length=800)),
            ],
        ),
    ]
