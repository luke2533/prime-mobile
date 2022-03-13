from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItems

@receiver(post_save, sender=OrderItems)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

@receiver(post_delete, sender=OrderItems)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()

# Taken from django mini projects
# Updates order total upon order item creation/change/deletion