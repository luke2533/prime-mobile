from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ("user",)
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address line 1",
            "default_street_address2": "Street Address line 2",
            "default_town_or_city": "Town or City",
            "default_postcode": "Postcode",
            "default_country": "Country",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "admin-input"
            self.fields[field].label = False

        # Sets default checkout info to database

# Used from django mini project