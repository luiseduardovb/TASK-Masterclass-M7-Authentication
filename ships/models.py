from django.conf import settings
from django.db import models


class SpaceShip(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    banner = models.ImageField(null=True, blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="space_ships",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
