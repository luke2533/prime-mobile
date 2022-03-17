from django.http import HttpResponse

from .models import Order, OrderItems
from store.models import Phone

import json
import time

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):

        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)


    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False

        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(content=f"Webhook received: {event['type']} | SUCCESS: Verified order already in database",
            status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f"Webhook received: {event['type']} | ERROR: {e}",
                status=500)

        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)


    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(
            content=f"Webhook received: {event['type']} | SUCCESS: Created order in webhook",
            status=200)


    # def handle_payment_intent_create(self, event):

    #     intent = event.data.object
    #     print(intent)

    #     return HttpResponse(
    #         content=f"Webhook received: {event['type']}",
    #         status=200)