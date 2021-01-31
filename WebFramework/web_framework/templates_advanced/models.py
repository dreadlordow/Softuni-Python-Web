from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=15, blank=False)
    is_done = models.BooleanField(default=False, blank=False)
    description = models.TextField()
