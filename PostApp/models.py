from django.db import models

# Create your models here.
from django.urls import reverse


class Catagory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catagory')

class Posts(models.Model):
    title = models.CharField(max_length=255)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

