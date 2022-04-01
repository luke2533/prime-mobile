from django.db import models

from profiles.models import UserProfile
from store.models import Phone


class PhoneReview(models.Model):

    class Meta:
        verbose_name_plural = "Phone Reviews"
        ordering = ["rating"]

    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                  null=False, blank=False)
    phone_name = models.ForeignKey(Phone, on_delete=models.CASCADE,
                                   null=True, blank=False)
    review_title = models.CharField(max_length=64, null=False, blank=False)
    review_body = models.TextField()
    rating = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.phone_name} review by {self.user_name}"

    # Add's phone review to database
