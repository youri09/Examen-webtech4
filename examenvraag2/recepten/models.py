from django.db import models

# Create your models here.
class Recept(models.Model):
    recept_name = models.CharField(max_length = 200)
    cals = models.IntegerField()
    ingredienten = models.CharField(max_length = 500)
    b_tijd = models.CharField(max_length = 20)
    def __str__(self):
        return self.recept_name
