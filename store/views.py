from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

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
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse("phones"))

            queries = Q(name__icontains=query)
            phones = phones.filter(queries)

    current_sorting = f"{sort}_{direction}"
    # Search and filter from Mini Project

    context = {
        "phones": phones,
        "search_term": query,
        "current_sorting": current_sorting,
    }

    return render(request, "store/store.html", context)


def phone_detail(request, phone_id):

    # Phone detail's info from phone model displays

    phone = get_object_or_404(Phone, pk=phone_id)
    reviews = PhoneReview.objects.all()
    total_rating = []
    phone_rating = 0

    for review in reviews:
        if review.phone_name == phone:
            user_rating = review.rating
            total_rating.append(user_rating)

            star_total = sum(total_rating)
            review_total = len(total_rating)
            overall_rating = star_total / review_total
            phone_rating = round(overall_rating)
            phone.rating = phone_rating
            phone.save()

    context = {
        "phone": phone,
        "reviews": reviews,
        "phone_rating": phone_rating,
    }

    return render(request, "store/phone_detail.html", context)


@login_required
def add_phone(request):

    # Admin can add phones to store and datebase

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

    # Admin can update information phones from store page and database

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
        messages.info(
            request, f"You are editing { phone.name } - { phone.pk }")

    template = "store/edit_phone.html"
    context = {
        "form": form,
        "phone": phone,
    }

    return render(request, template, context)


@login_required
def delete_phone(request, phone_id):

    # Admin can delete phones from store page and database

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store admins can do that")
        return redirect(reverse("home"))

    phone = get_object_or_404(Phone, pk=phone_id)
    phone.delete()
    messages.success(request, "Phone removed from store")
    return redirect(reverse("store"))
