from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.user