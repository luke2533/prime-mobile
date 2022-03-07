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

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    rating = models.IntegerField(default=1, blank=True, null=True)
    
    os = models.CharField(max_length=254, null=True, blank=True)
    screen = models.CharField(max_length=254, null=True, blank=True)
    camera = models.CharField(max_length=254, null=True, blank=True)
    capacity = models.CharField(max_length=254, null=True, blank=True)
    img_1 = models.ImageField(null=True, blank=True)
    img_2 = models.ImageField(null=True, blank=True)
    img_3 = models.ImageField(null=True, blank=True)

    storage_1 = models.IntegerField(default=1, blank=True, null=True)
    storage_2 = models.IntegerField(default=1, blank=True, null=True)
    storage_3 = models.IntegerField(default=1, blank=True, null=True)
    storage_4 = models.IntegerField(default=1, blank=True, null=True)
    color_1 = models.CharField(max_length=254, null=True, blank=True)
    color_2 = models.CharField(max_length=254, null=True, blank=True)
    color_3 = models.CharField(max_length=254, null=True, blank=True)
    color_4 = models.CharField(max_length=254, null=True, blank=True)
    price_1 = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    price_2 = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    price_3 = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    price_4 = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    display_store = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return self.name