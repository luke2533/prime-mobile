from django.shortcuts import render, get_object_or_404, redirect
from store.models import Phone

def user_bag(request):
    
    return render(request, "bag/bag.html")


def add_phone_bag(request, item_id):

    phone = get_object_or_404(Phone, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session["bag"] = bag
    print(request.session["bag"])
    return redirect(redirect_url)
    # Need to figure out how to get simfree fixtures