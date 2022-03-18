from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_phones, name="store"),
    path("<int:phone_id>/", views.phone_detail, name="phone_detail"),
    path("add/", views.add_phone, name="add_phone"),
]