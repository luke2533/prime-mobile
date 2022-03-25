from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from store.views import phone_detail
from .models import PhoneReview
from .forms import ReviewForm
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
    phone = get_object_or_404(Phone, pk=phone_id)
    user = get_object_or_404(UserProfile, user=request.user)

    review_data = {
        "user_name": user,
        "phone_name": phone,
        "review_title": request.POST.get("review_title"),
        "review_body": request.POST.get("review_body"),
        "rating": request.POST.get("rating"),
    }

    if request.method == "POST":
        review_form = ReviewForm(review_data)
        
        print(review_form.errors)

        if review_form.is_valid():
            phone_review = review_form.save()

            phone_review.save()

            messages.success(request, "Review successful")
            return redirect("phone_detail", phone_id)
        else:
            messages.error(request, "Review failed to POST")

    return redirect("review", phone_id)


def delete_review(request, review_id):
    reviews = get_object_or_404(PhoneReview, pk=review_id)

    reviews.delete()
    messages.success(request, "Review successfully removed")
    return redirect("store")