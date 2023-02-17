from django.db import models
from datetime import datetime
# Create your models here.


class TodoApp(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=500000)
    created_at = models.DateTimeField(
        blank=True, default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
