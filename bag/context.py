from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Phone

def bag_contents(request):
    # Makes bag contents dictionary availible to all templates

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        phone = get_object_or_404(Phone, pk=item_id)
        price = phone.price_1 or phone.price_2 or phone.price_3 or phone.price_4
        color = phone.color_1 or phone.color_2 or phone.color_3 or phone.color_4
        storage = phone.storage_1 or phone.storage_2 or phone.storage_3 or phone.storage_4
        total += quantity * price
        # Need to figure out price 1 to 4
        product_count += quantity
        bag_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "phone": phone,
            "price": price,
            "color": color,
            "storage": storage,
        })

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY,
        "grand_total": grand_total
    }

    return context
# Used from django mini project