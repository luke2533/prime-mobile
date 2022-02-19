from django.db import models

# Create your models here.

class Category(models.Model):
    
    # Categories for products such as SIM Free and Deals

    class Meta:
        verbose_name_plural = "Categories"


    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Phone(models.Model):

    # Phone data

    class Meta:
        verbose_name_plural = "Phone"

    phone_model = models.IntegerField(default=1, blank=True, null=True)
    name = models.CharField(max_length=254)
    from_cost = models.FloatField(default=1, blank=True, null=True)
    rating = models.FloatField(default=1, blank=True, null=True)
    
    os = models.CharField(max_length=254, null=True, blank=True)
    screen = models.CharField(max_length=254, null=True, blank=True)
    camera = models.CharField(max_length=254, null=True, blank=True)
    capacity = models.CharField(max_length=254, null=True, blank=True)
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name


class SimFree(models.Model):

    # Sim Free data

    class Meta:
        verbose_name_plural = "SIM Free"

    phone_id = models.IntegerField(default=1, blank=True, null=True)
    phone_model = models.IntegerField(default=1, blank=True, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)

    storage = models.IntegerField(default=1, blank=True, null=True)
    color = models.CharField(max_length=254, null=True, blank=True)
    cost = models.FloatField(default=1, blank=True, null=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name