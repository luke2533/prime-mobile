from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_phones, name="store"),
    path("<product_id>", views.phone_detail, name="phone_detail"),
]