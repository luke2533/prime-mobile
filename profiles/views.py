from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Delivery info updated.")
        else:
            messages.error(request, "Update failed")
    else:
        form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    template = "profiles/profile.html"
    
    context= {
        "form": form,
        "orders": orders,
    }

    # Profile page

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f"Past confirmation for order number {order_number}"
    ))

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    # Account order history

    return render(request, template, context)
# Django mini project