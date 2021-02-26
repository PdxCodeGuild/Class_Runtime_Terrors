from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120) # Max_length.
	description = models.TextField(blank=True,null=True)
	price = models.DecimalField(max_digits=100000, decimal_places=2)
	summary = models.TextField(blank=True,null=True)
	featured = models.BooleanField()