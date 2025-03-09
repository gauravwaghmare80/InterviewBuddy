from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_candidate = models.BooleanField(default=False)  # Default value added

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    USERNAME_FIELD = 'username'  # Explicitly set the username field
    REQUIRED_FIELDS = []  # Optional fields

    def __str__(self):
        return self.username  # Fixed incorrect field reference
