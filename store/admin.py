from django.contrib import admin
from .models import Category, Phone, SimFree

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        "phone_model",
        "name",
        "from_cost",
        "rating",
        "category",
    )

    ordering = ("phone_model",)

class SimFreeAdmin(admin.ModelAdmin):
    list_display = (
        "phone_id",
        "phone_model",
        "sku",
        "name",
        "storage",
        "color",
        "cost",
        "category",
    )

    ordering = ("phone_id",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(SimFree, SimFreeAdmin)
