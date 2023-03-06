from django.db import models


class User(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    customer_id = models.CharField(max_length=255)
