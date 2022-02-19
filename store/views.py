from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Phone


def all_phones(request):
    
    # Displays all of the phones on store page

    phones = Phone.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                phones = phones.annotate(lower_name=Lower("name"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            phones = phones.order_by(sortkey)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("phones"))

            queries = Q(name__icontains=query)
            phones = phones.filter(queries)
    
    current_sorting = f"{sort}_{direction}"
    # Search and filter Mini Project

    context = {
        "phones": phones,
        "search_term": query,
        "current_sorting": current_sorting,
    }

    return render(request, "store/store.html", context)

    
def phone_detail(request, product_id):

    # Phone detail page

    phone = get_object_or_404(Phone, pk=product_id)
    
    context = {
        "phone": phone,
    }

    return render(request, "store/phone_detail.html", context)
