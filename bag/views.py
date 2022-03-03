from django.shortcuts import render, get_object_or_404
from store.models import Phone

def user_bag(request):
    
    return render(request, "bag/bag.html")


# def add_phone_bag(request, item_id):

    # phone = get_object_or_404(Phone, pk=item_id)
    # Need to figure out how to get simfree fixtures