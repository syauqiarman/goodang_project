from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)