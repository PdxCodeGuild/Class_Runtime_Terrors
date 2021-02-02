from django.db import models
from django.urls import reverse

class Quantity(models.Model):

    OUNCE = 'Ounce'
    QUARTER = 'Quarter'
    EIGHTH = 'Eighth'
    GRAM = 'Gram'
    CARTRIDGE = 'Cartridge'
    PACKAGE = 'Package'
    PREROLL = 'Preroll'

    WEIGHT = [
        (OUNCE, 'Ounce'),
        (QUARTER, 'Quarter'),
        (EIGHTH, 'Eighth'),
        (GRAM, 'Gram'),
        (CARTRIDGE, 'Cartridge'),
        (PACKAGE, 'Package'), 
        (PREROLL, 'Preroll'),
    ]

    name = models.CharField(max_length=9, choices=WEIGHT, default=GRAM) # Ounce, Quarter, Cartridge, Package
    slug = models.SlugField(max_length=200, unique=True) # Used to create unique url for search


    class Meta:
        ordering = ('name',)
        verbose_name = 'quantity'
        verbose_name_plural = 'quantities'

    def __str__(self):
        return self.name

class Category(models.Model):

    FLOWER = 'Flower'
    CONCENTRATE = 'Concentrate'
    CARTRIDGE = 'Cartridge'
    EDIBLE = 'Edible'
    OTHER = 'Other'
    PREROLL = 'Preroll'

    TYPE_OF_CANNABIS = [
        (FLOWER, 'Flower'),
        (CONCENTRATE, 'Concentrate'),
        (CARTRIDGE, 'Cartridge'),
        (EDIBLE, 'Edible'),
        (OTHER, 'Other'),
        (PREROLL, 'Preroll'),
    ]
    name = models.CharField(max_length=11, choices=TYPE_OF_CANNABIS, default=FLOWER) # Flower, Concentrate, Edible
    slug = models.SlugField(max_length=200, unique=True) # Used to create unique url for search

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('online_shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Variety(models.Model):

    INDICA = 'Indica'
    SATIVA = 'Sativa'
    HYBRID = 'Hybrid'
    
    KIND_OF_CANNABIS = [
        (INDICA, 'Indica'),
        (SATIVA, 'Sativa'),
        (HYBRID, 'Hybrid'),
    ]

    name = models.CharField(max_length=6, choices=KIND_OF_CANNABIS, default=HYBRID) # Hybrid, Indica, Sativa
    slug = models.SlugField(max_length=200, unique=True) # Used to create unique url for search
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'variety'
        verbose_name_plural = 'varieties'
    
    def get_variety_url(self):
        print(self, 'HELLO')
        return reverse('online_shop:variety_detail',
        args=[self.slug])
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # Flower, Concentrate, Edible
    variety = models.ForeignKey(Variety, related_name='products', on_delete=models.CASCADE) # Hybrid, Indica, Sativa
    quantity = models.ForeignKey(Quantity, related_name='products', on_delete=models.CASCADE) # Weight in GRAMS/ packaging
    name = models.CharField(max_length=200, db_index=True) #Strain
    slug = models.SlugField(max_length=200, db_index=True) #Auto-generated url 'www.w/slug'
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='../media/no_image.jpg') #Pic of product

    thc = models.DecimalField(max_digits=6, decimal_places=2) # THC % 33.42% THC
    cbd = models.DecimalField(max_digits=6, decimal_places=2) # CBD % 7.66% CBD
    price = models.IntegerField() # Price in Dollars
    available = models.BooleanField(default=True) # More than 1 GRAM in inventory? T/F
    created  = models.DateTimeField(auto_now_add=True) # Auto Timestamp upon creation
    updated = models.DateTimeField(auto_now=True) # Auto Timestamp upon changes

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('online_shop:product_detail',
        args=[self.id, self.slug,])

    def __str__(self):
        return self.name

