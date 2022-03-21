from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Phone
from .forms import StoreForm
from reviews.models import PhoneReview

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

    
def phone_detail(request, phone_id):

    phone = get_object_or_404(Phone, pk=phone_id)
    reviews = PhoneReview.objects.all()

    context = {
        "phone": phone,
        "reviews": reviews,
    }

    return render(request, "store/phone_detail.html", context)


@login_required
def add_phone(request):

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store admins can do that")
        return redirect(reverse("home"))    

    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.save()
            messages.success(request, "Successfully Added Phone")
            return redirect(reverse("phone_detail", args=[phone.id]))
        else:
            messages.error(request, "Failed to add phone")
    else:
        form = StoreForm()

    template = "store/add_phone.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_phone(request, phone_id):

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store admins can do that")
        return redirect(reverse("home"))

    phone = get_object_or_404(Phone, pk=phone_id)

    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            messages.success(request, "Succesfully updated phone")
            return redirect(reverse("phone_detail", args=[phone.id]))
        else:
            messages.error(request, "Failed to update phone")
    else:
        form = StoreForm(instance=phone)
        messages.info(request, f"You are editing { phone.name } - { phone.pk }")

    template = "store/edit_phone.html"
    context = {
        "form": form,
        "phone": phone,
    }

    return render(request, template, context)


@login_required
def delete_phone(request, phone_id):

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store admins can do that")
        return redirect(reverse("home"))    

    phone = get_object_or_404(Phone, pk=phone_id)
    phone.delete()
    messages.success(request, "Phone removed from store")
    return redirect(reverse("store"))