from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Phone


def all_phones(request):
    
    # Displays all of the phones on store page

    phones = Phone.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("phones"))

            queries = Q(name__icontains=query)
            phones = phones.filter(queries)
    
    context = {
        "phones": phones,
        "search_term": query,
    }

    return render(request, "store/store.html", context)

    
def phone_detail(request, product_id):

    # Phone detail page

    phone = get_object_or_404(Phone, pk=product_id)
    
    context = {
        "phone": phone,
    }

    return render(request, "store/phone_detail.html", context)
