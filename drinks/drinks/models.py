from django.db import models

class Drinks(models.Model):
    name=models.CharField(max_length=300,unique=True)
    age=models.IntegerField()

    def __str__(self):
        return self.name
