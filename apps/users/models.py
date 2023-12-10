from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ("Student", "Estudiante"),
        ("Technical", "Técnico"),
    )
    phone = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, null=False, blank=False,default="Student"
    )
