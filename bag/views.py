from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.contrib import messages
from store.models import Phone

def user_bag(request):
    
    return render(request, "bag/bag.html")


def add_phone_bag(request, item_id):

    phone = get_object_or_404(Phone, pk=item_id)
    color = request.POST.get("color")
    storage = int(request.POST.get("storage"))
    price = float(request.POST.get("price"))
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id]["quantity"] += quantity
        messages.success(request, f'Updated quantity of {phone.name}')
        # If the item is already in the bag

    else:
        bag[item_id] = {"color": color, "storage": storage, "price": price, "quantity": quantity}
        messages.success(request, f'{phone.name} added to your bag')

        # Adding a new phone
            
    request.session["bag"] = bag
    return redirect(redirect_url)


def edit_phone_bag(request, item_id):

    phone = get_object_or_404(Phone, pk=item_id)
    color = request.POST.get("color")
    storage = int(request.POST.get("storage"))
    price = float(request.POST.get("price"))
    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated quantity of {phone.name}')

    else:
        del bag[item_id]
        if not bag[item_id]:
            bag.pop(item_id)
        messages.success(request, f'Removed {phone.name} from your bag')
            
    request.session["bag"] = bag
    return redirect(reverse("user_bag"))


def delete_phone_bag(request, item_id):
    
    phone = get_object_or_404(Phone, pk=item_id)
    bag = request.session.get("bag", {})
    bag.pop(item_id)
    # message goes here
    messages.success(request, f'{phone.name} removed from your bag')

    request.session["bag"] = bag
    return HttpResponse(status=200)