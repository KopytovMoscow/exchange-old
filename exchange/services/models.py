from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    executor_id = models.CharField(max_length=255)