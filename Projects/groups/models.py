from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class GroupListing(models.Model):
    def __str__(self):
        return self.groupName

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)

    groupName = models.CharField(max_length = 20)
    image = models.ImageField(default='default.jpg', upload_to='consultant_pics')

    description = models.TextField()
    termsAndConditions = models.BooleanField()

    def get_absolute_url(self):
        return reverse('cons-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
