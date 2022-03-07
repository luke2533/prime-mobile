from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_phones, name="store"),
    path("<phone_id>", views.phone_detail, name="phone_detail"),
]