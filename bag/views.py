from django.shortcuts import render

def user_bag(request):
    
    return render(request, "bag/bag.html")