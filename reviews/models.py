from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

from store.models import Phone
from profiles.models import UserProfile


class PhoneReview(models.Model):

    class Meta:
        verbose_name_plural = "Phone Reviews"
        ordering = ["-date"]

    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    phone_name = models.ForeignKey(Phone, null=False, blank=False, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=64, null=False, blank=False)
    review_body = models.TextField()
    rating = models.IntegerField(default=1, blank=True, null=True, validators=[
        MaxValueValidator(5),
        MinLengthValidator(1),
    ])

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name