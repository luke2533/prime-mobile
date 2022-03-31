from django import forms
from .models import PhoneReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = PhoneReview
        fields = ("user_name", "phone_name", "review_title", "review_body", "rating",)

    # Review form