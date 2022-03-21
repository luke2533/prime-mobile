from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:phone_id>', views.reviews, name='reviews'),
]