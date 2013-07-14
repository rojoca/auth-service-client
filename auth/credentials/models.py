from django.db import models


class Credential(models.Model):
    username = models.CharField(unique=True, max_length=20)
    password_hash = models.CharField(max_length=255)
