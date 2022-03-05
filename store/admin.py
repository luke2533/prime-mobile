from django.contrib import admin
from .models import Category, Phone

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "storage_1",
        "color_1",
        "price_1",
        "category",
    )

    ordering = ("sku",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Phone, PhoneAdmin)
