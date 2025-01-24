from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()
    gender = models.CharField(max_length= 10)
    salary = models.FloatField()

    def __str__(self):
        return self.last_name
