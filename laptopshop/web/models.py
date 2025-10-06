from django.db import models

# Create your models here.
class laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    ram = models.IntegerField()
    ssd = models.IntegerField()
    harddisk = models.IntegerField()
    operating = models.CharField(max_length=255)
    graphics = models.CharField(max_length=255)
    screen = models.IntegerField()
    resolution = models.CharField(max_length=255)
    nocores = models.IntegerField()
    nothreads = models.IntegerField()
    specscore = models.IntegerField()
    price = models.IntegerField()

    @property
    def price_view(self):
        return "{:,}".format(self.price).replace(",", ".")