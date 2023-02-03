from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    user_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)

