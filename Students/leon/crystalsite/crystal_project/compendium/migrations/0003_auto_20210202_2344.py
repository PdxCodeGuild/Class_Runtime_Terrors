# Generated by Django 3.1.6 on 2021-02-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0002_tag_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crystal',
            name='tags',
            field=models.ManyToManyField(blank=True, to='compendium.Tag'),
        ),
    ]
