from django.shortcuts import render, get_object_or_404
from . models import Category, Quantity, Variety, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None, variety_slug=None):
    category = None
    variety = None
    categories = Category.objects.all()
    varieties = Variety.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    elif variety_slug:
        variety = get_object_or_404(Variety, slug = variety_slug)
        products = products.filter(variety=variety)
    return render(request, 'product/list.html',{
        'category': category,
        'categories': categories,
        'products': products,
        'variety': variety,
        'varieties': varieties,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True,)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form})

