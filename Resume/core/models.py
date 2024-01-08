from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=100)
    subject=models.TextField(max_length=100)
    message=models.CharField(max_length=300, default='default_message_value')

    def __str__(self):
        return self.message