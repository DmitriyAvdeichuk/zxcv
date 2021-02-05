from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Testmodel(models.Model):
    field = models.TextField(max_length=255)
    data = JSONField()

    def __str__(self):
        return self.field, self.data
