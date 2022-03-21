from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import PhoneReview
from store.models import Phone
from profiles.models import UserProfile


@login_required
def add_review(request, phone_id):

    phone = get_object_or_404(Phone, pk=phone_id)
    user = get_object_or_404(UserProfile, user=request.user)
    phone_name = phone.name
    title = request.POST.get("title")
    body = request.POST.get("body")
    rating = request.POST.get("rating")

    if request.method == "POST":

        print(phone)
        print(user)

    template = "reviews/reviews.html"
    context = {
        "phone": phone,
    }

    return render(request, template, context)
