import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name="Eメール")
    icon = models.ImageField(upload_to="account/icon/", null=True, blank=True, default="icon/example.png")
