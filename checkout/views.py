from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from .models import Order, OrderItems

from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from store.models import Phone
from bag.context import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            "bag": json.dumps(request.session.get("bag", {})),
            "save_info": request.POST.get("save_info"),
            "username": request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry your payment cannot be proccessed right now.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})
        
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "town_or_city": request.POST["town_or_city"],
            "postcode": request.POST["postcode"],
            "country": request.POST["country"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    phone = Phone.objects.get(id=item_id)
                    order_item = OrderItems(
                        order=order,
                        phone=phone,
                        phone_color=item_data["color"],
                        phone_storage=item_data["storage"],
                        phone_quantity=item_data["quantity"],
                        phone_price=item_data["price"],
                    )

                    order_item.save()
                except Phone.DoesNotExist:
                    messages.error(request, (
                        "One of the phone's in your bag wasn't found in our database. "
                        "Please contact customer support."
                    ))
                    order.delete()
                    return redirect(reverse(""))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
            # Havn't made the checkout success page yet
        else:
            messages.error(request, "There was an error with your form.")
    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(request, "There's nothing in your bag")
            return redirect(reverse("store"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    "full_name": profile.user.get_full_name(),
                    "email": profile.user.email,
                    "phone_number": profile.default_phone_number,
                    "country": profile.default_country,
                    "postcode": profile.default_postcode,
                    "town_or_city": profile.default_town_or_city,
                    "street_address1": profile.default_street_address1,
                    "street_address2": profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing.")

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            "default_phone_number": order.phone_number,
            "default_country": order.country,
            "default_postcode": order.postcode,
            "default_town_or_city": order.town_or_city,
            "default_street_address1": order.street_address1,
            "default_street_address2": order.street_address2,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
        # Django mini project
    
    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
