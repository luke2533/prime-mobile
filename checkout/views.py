from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe

def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse("store"))

    current_bag = bag_contents(request)
    total = current_bag["grand_total"]
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51KKEOAHzs9HEGl4YCTuTP5baVBtseZIc5yePs2r1fNuwwNq0xvXHA1uC8ANDl1Z0A2qQUoBVlStsT8yDdDZVb2mH00wrAcVSxc",
        "client_secret": "test",
    }

    return render(request, template, context)
