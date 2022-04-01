from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_bag, name="bag"),
    path("add/<item_id>/", views.add_phone_bag, name="add_phone_bag"),
    path("edit/<item_id>/", views.edit_phone_bag, name="edit_phone_bag"),
    path("delete/<item_id>/", views.delete_phone_bag, name="delete_phone_bag"),
]
