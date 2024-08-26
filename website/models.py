from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject= models.TextField(max_length=300)
    message = models.TextField(max_length=10000)
    