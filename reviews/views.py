from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import PhoneReview
from store.models import Phone
from profiles.models import UserProfile


@login_required
def review(request, phone_id):
    phone = get_object_or_404(Phone, pk=phone_id)
    user = get_object_or_404(UserProfile, user=request.user)
    
    template = "reviews/reviews.html"
    context = {
        "phone": phone,
        "user": user,
    }

    return render(request, template, context)


@login_required
def add_review(request, phone_id):

    if request.method == "POST":
        phone = get_object_or_404(Phone, pk=phone_id)
        user = get_object_or_404(UserProfile, user=request.user)
        phone_name = request.POST.get("phone")
        review_title = request.POST.get("title")
        review_body = request.POST.get("body")
        rating = request.POST.get("rating")

        return HttpResponse(status=200)

    return redirect("review", phone_id)