from django import forms
from .models import Phone, Category


class StoreForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # Django mini project

        self.fields["category"].choices = friendly_names
        for field_name, filed in self.fields.items():
            filed.widget.attrs["class"] = "border-black rounded-0 admin-input"
