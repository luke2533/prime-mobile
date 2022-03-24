from django.contrib import admin
from .models import PhoneReview


class PhoneReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "phone_name",
        "rating",
    )

    ordering = ("rating",)


admin.site.register(PhoneReview, PhoneReviewAdmin)
