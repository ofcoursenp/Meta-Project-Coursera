from django.db import models

# Create your models here.

class item(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Description = models.TextField(max_length=30000)
    Image = models.ImageField(upload_to='main/images')

    def __str__(self):
        return self.Name


class Booking(models.Model):
    Name = models.CharField(max_length=60)
    Date = models.DateField()
    time = models.TimeField()
    Phone_number = models.IntegerField()

    def __str__(self):
        return self.Name













