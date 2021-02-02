# Generated by Django 3.1.4 on 2021-01-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageloader', '0002_auto_20210122_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_cover', models.ImageField(blank=True, null=True, upload_to='galleries/')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
