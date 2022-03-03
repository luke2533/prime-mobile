from django.shortcuts import render, get_object_or_404
from store.models import SimFree, Phone

def user_bag(request):
    
    return render(request, "bag/bag.html")


def add_phone_bag(request, item_id):

    simfree = get_object_or_404(SimFree, pk=item_id)
    # Need to figure out how to get simfree fixtures
