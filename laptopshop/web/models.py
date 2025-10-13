from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    ram = models.IntegerField()
    ssd = models.IntegerField()
    graphics = models.CharField(max_length=255)
    screen = models.FloatField()
    resolution = models.CharField(max_length=255)
    nocores = models.IntegerField()
    nothreads = models.IntegerField()
    specscore = models.IntegerField()
    price = models.IntegerField()
    imageurl = models.CharField(max_length=255)

    @property
    def price_view(self):
        return "{:,}".format(self.price).replace(",", ".")
    
    def __str__(self):
        return f"{self.name} | {self.brand} | {self.price_view}đ"