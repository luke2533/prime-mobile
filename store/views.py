from django.shortcuts import render, get_object_or_404
from .models import SimFree


def all_phones(request):

    phones = SimFree.objects.all()
    
    context = {
        "phones": phones,
    }

    return render(request, "store/store.html", context)

    
def phone_detail(request, product_id):

    phone = get_object_or_404(SimFree, pk=product_id)
    
    context = {
        "phone": phone,
    }

    return render(request, "store/phone_detail.html", context)
