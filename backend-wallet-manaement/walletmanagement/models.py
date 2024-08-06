
from django.db import models
from django.contrib.auth.hashers import make_password

class UserPassword(models.Model):
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
