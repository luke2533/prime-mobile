from django.shortcuts import render
from .models import SimFree


def all_phones(request):

    phones = SimFree.objects.all()
    
    context = {
        "phones": phones,
    }

    return render(request, "store/store.html", context)
