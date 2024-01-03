from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ("Student", "Estudiante"),
        ("Technical", "Técnico"),
    )
    phone = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        null=False,
        blank=False,
        default="Technical",
    )

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(
            ("pbkdf2_sha256$", "bcrypt$", "argon2")
        ):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
