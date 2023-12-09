from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(max_length=50)


class Reminder(models.Model):
    description = models.TextField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    