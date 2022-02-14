from django.shortcuts import render, get_object_or_404
from .models import Phone


def all_phones(request):
    
    # Displays all of the phones on store page

    phones = Phone.objects.all()
    
    context = {
        "phones": phones,
    }

    return render(request, "store/store.html", context)

    
def phone_detail(request, product_id):

    # Phone detail page

    phone = get_object_or_404(Phone, pk=product_id)
    
    context = {
        "phone": phone,
    }

    return render(request, "store/phone_detail.html", context)
