from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
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
    phone_name = phone.name
    name = phone_name

    review_data = {
        "user_name": user,
        "phone_name": "",
        "review_title": request.POST.get("review_title"),
        "review_body": request.POST.get("review_body"),
        "rating": request.POST.get("rating"),
    }

    if request.method == "POST":
        review_form = ReviewForm(review_data)
        
        print(phone_name)
        
        if review_form.is_valid():
            phone_review = review_form.save(commit=False)

            phone_review.phone_name = name

            print(phone_name)
            print("Success")

            phone_review.save()

            messages.success(request, "Review successful")
            return redirect("phone_detail", phone_id)
        
        else:
            messages.error(request, "Review failed to POST")

    review_form.errors.as_data()
    print(name)
    return redirect("review", phone_id)