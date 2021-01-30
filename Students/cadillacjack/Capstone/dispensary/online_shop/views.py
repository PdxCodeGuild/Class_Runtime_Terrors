from django.shortcuts import render, get_object_or_404
from . models import Category, Quantity, Variety, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html',{
        'category': category,
        'categories': categories,
        'products': products,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True,)
    return render(request, 'product/detail.html', {'product': product})

def variety_list(request, variety_slug=None):
    variety = None
    varieties = Variety.objects.all()
    products = Product.objects.filter(available=True)
    if variety_slug:
        variety = get_object_or_404(Variety, slug = variety_slug)
        products = products.filter(variety=variety)
    return render(request, 'product/variety.html',{
        'variety': variety,
        'varieties': varieties,
        'products': products,
    })

def variety_detail(request, slug):
    variety = get_object_or_404(Variety, slug=slug, available=True,)
    return render(request, 'product/variety.html', {'variety': variety})


