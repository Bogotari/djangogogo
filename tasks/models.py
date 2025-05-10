from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title