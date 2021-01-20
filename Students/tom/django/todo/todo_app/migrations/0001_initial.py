# Generated by Django 3.1.5 on 2021-01-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('todo_type', models.CharField(blank=True, choices=[('p', 'personal'), ('s', 'school'), ('w', 'work'), ('f', 'family'), ('m', 'misc')], default='m', max_length=1)),
            ],
        ),
    ]
