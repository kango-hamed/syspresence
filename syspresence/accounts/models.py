from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('enseignant', 'Enseignant'),
        ('educateur', 'Éducateur'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='educateur')

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Définit un related_name spécifique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Définit un related_name spécifique
        blank=True,
    )

