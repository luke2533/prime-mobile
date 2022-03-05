from django.contrib import admin
from .models import Category, Phone

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        "phone_model",
        "sku",
        "name",
        "storage",
        "color_1",
        "color_2",
        "color_3",
        "color_4",
        "price",
        "category",
    )

    ordering = ("phone_model",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Phone, PhoneAdmin)
