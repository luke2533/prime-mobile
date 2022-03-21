from django.contrib import admin
from .models import PhoneReview


class PhoneReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "date",
        "phone_name",
        "rating",
    )

    ordering = ("date",)

admin.site.register(PhoneReview, PhoneReviewAdmin)