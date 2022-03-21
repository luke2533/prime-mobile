from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from store.models import Phone
from profiles.models import UserProfile


@login_required
def reviews(request, phone_id):
# def reviews(request):

    phone = get_object_or_404(Phone, pk=phone_id)
    user_name = UserProfile.objects.get(user=request.user)
    # date = 
    phone_name = phone.name
    title = request.POST.get("")
    body = request.POST.get("")
    rating = request.POST.get("")

    template = "reviews/reviews.html"
    context = {
        "phone": phone,
    }

    return render(request, template, context)
    # return render(request, template)
