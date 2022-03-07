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
        total += quantity * phone.price_1
        # Quantity no a variable
        product_count += quantity
        bag_items.append({
            "item_id": item_id,
            "quantity": quantity,
            "phone": phone,
            # "color": color,
            # "storage": storage,
            # "price": price,
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