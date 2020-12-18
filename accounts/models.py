from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from rest_framework import validators


class User(models.Model):
    """Модель пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_creator = models.BooleanField(default=False)
    # email = models.EmailField(
    #         validators=[validators.validate_email],
    #         unique=True,
    #         blank=False
    #     )

    def __str__(self):
        return self.user.username
        return self.user.location
