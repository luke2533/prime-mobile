from django.contrib import admin
from .models import Category, SimFree

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "freindly_name",
        "name",
    )


class SimFreeAdmin(admin.ModelAdmin):
    list_display = (
        "phone_id",
        "sku",
        "name",
        "category",
        "storage",
        "color",
        "cost",
    )

    ordering = ("phone_id",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SimFree, SimFreeAdmin)
