from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:phone_id>/', views.review, name='review'),
    path('add_review/<int:phone_id>/', views.add_review, name='add_review'),
]