from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from store.models import Phone


@login_required
def reviews(request, phone_id):
# def reviews(request):

    phone = get_object_or_404(Phone, pk=phone_id)

    template = "reviews/reviews.html"
    context = {
        "phone": phone,
    }

    return render(request, template, context)
    # return render(request, template)
