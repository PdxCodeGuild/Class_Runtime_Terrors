from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from compendium.models import Tag
from .models import HoundSite 



def rockhound_list(request):
    sites = HoundSite.objects.all()
    context = {
        "sites": sites,
    }
    return render(request, 'rockHound/rockHound_list.html', context)
     

def site_detail(request, slug):
    site = get_object_or_404(HoundSite, slug__iexact=slug)
    address = site.address
    context = {
        'site': site,
        'address': address
    }
    return render(request, 'rockHound/site_detail.html', context)


@login_required
def createSite(request):
    if request.method == "POST":
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        address = request.POST.get('address')
        rocks = request.POST.get('rocks')
        notes = request.POST.get('notes')
    
        new_Site = HoundSite.objects.create(
            name=name,
            slug=slug,
            address=address,
            notes=notes,
            rocks=rocks
        )
        sites = HoundSite.objects.all()
        context = {
            "sites": sites,
        }
        return render(request, 'rockHound/rockHound_list.html', context)
    else:
        return render(request, 'rockHound/create_site.html')

