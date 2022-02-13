from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=254)
    freindly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class sim_free(models.Model):
    phone_id = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)

    os = models.CharField(max_length=254, null=True, blank=True)
    screen = models.FloatField(blank=True, null=True)
    camera = models.CharField(max_length=254, null=True, blank=True)
    capacity = models.CharField(max_length=254, null=True, blank=True)
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)

    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    storage = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=254, null=True, blank=True)
    # Come back to this one
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
