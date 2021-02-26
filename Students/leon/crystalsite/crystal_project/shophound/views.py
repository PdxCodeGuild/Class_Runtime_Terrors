from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from compendium.models import Tag
from .models import RockShop 


def shophound_list(request):
    shops = RockShop.objects.all()
    context = {
        "shops": shops,
    }
    return render(request, 'shophound/rockshop_list.html', context)
     

def shop_detail(request, slug):
    shop = get_object_or_404(RockShop, slug__iexact=slug)
    website = shop.website
    address = shop.address
    context = {
        'shop': shop,
        'website': website,
        'address': address
    }
    return render(request, 'shophound/shop_detail.html', context)


@login_required
def createShop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        address = request.POST.get('address')
        website = request.POST.get('website')
        hours = request.POST.get('hours')
        description = request.POST.get('description')
    
        new_Shop = RockShop.objects.create(
            name=name,
            slug=slug,
            address=address,
            website=website,
            hours=hours,
            description=description
        )
        shops = RockShop.objects.all()
        context = {
            "shops": shops,
        }
        return render(request, 'shophound/rockshop_list.html', context)
    else:
        return render(request, 'shophound/create_shop.html')


