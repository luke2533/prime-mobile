from django.contrib import admin
from .models import Order, OrderItems

class OrderItemsAdmin(admin.TabularInline):
    
    model = OrderItems
    readonly_fields = ("phone_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsAdmin,)

    readonly_fields = ("order_number", "date", "delivery_cost", "order_total", "grand_total",)

    fields = ("order_number", "date", "full_name", "email", "phone_number", "country", "postcode", 
                "town_or_city", "street_address1", "street_address2", "delivery_cost", "order_total", 
                "grand_total",)

    list_display = ("order_number", "date", "full_name", "order_total", "delivery_cost", "grand_total",)

    ordering = ("-date",)

# Model and admin used from django mini project
admin.site.register(Order, OrderAdmin)