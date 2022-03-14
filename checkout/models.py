import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from store.models import Phone

class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # User order information

    def _order_id(self):
        return uuid.uuid4().hex.upper()
        # Generates order id
    
    def update_total(self):
        self.order_total = self.orderitems.aggregate(Sum("phone_total"))["phone_total__sum"] or 0
        if self.order_total < settings.FREE_DELIVERY:
            self.delivery_cost = self.order_total * settings.DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._order_id()
        super().save(*args, **kwargs)
        # Sets the order id

    def __str__(self):
        return self.order_number


class OrderItems(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name="orderitems")
    phone = models.ForeignKey(Phone, null=False, blank=False, on_delete=models.CASCADE)
    phone_color = models.CharField(max_length=7, null=False, blank=False)
    phone_size = models.IntegerField(null=False, blank=False)
    phone_quantity = models.IntegerField(null=False, blank=False)
    phone_price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    phone_total = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.phone_total = self.phone_price * self.phone_quantity
        super().save(*args, **kwargs)
        # Sets the order id

    def __str__(self):
        return f"SKU {self.phone.sku} on order {self.order.order_number}"