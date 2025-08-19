from django.db import models
from django.template.base import kwarg_re
from django.template.defaultfilters import lower


# Create your models here.
class Clients(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False
    )
    email = models.CharField(
        unique=True,
        max_length=256
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=256
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if self.email:
            self.email=self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.email}'
