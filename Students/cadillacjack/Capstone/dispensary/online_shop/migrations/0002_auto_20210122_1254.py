# Generated by Django 3.1.5 on 2021-01-22 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('OZ', 'Ounce'), ('QT', 'Quarter'), ('EI', 'Eighth'), ('GR', 'Gram'), ('CA', 'Cartridge'), ('PA', 'Package'), ('PR', 'Preroll')], default='GR', max_length=2)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'quantity',
                'verbose_name_plural': 'quantities',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='online_shop.quantity'),
        ),
    ]