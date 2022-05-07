from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.


class Job(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    # Date
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField(auto_now=True)
    # Address
    street = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2), MaxLengthValidator(2)])
    zip = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(10000)])
    image = models.ImageField(upload_to='media', default='')
    summary = models.TextField(blank=True)

    def __str__(self):
        return f'{self.company}: {self.position}'
