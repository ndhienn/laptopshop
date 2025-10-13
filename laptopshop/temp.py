import csv
from web.models import Laptop

with open('data\output11.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Laptop.objects.create(
            name=row['model_name'],
            brand=row['brand'],
            processor=row['processor_name'],
            ram=row['ram(GB)'],
            ssd=row['ssd(GB)'],
            graphics=row['graphics'],
            screen=row['screen_size(inches)'],
            resolution=row['resolution (pixels)'],
            nocores=row['no_of_cores'],
            nothreads=row['no_of_threads'],
            specscore=row['spec_score'],
            price=row['price'],
            imageurl='',
        )
print("✅ Đã import CSV thành công!")
    # name = models.CharField(max_length=255)
    # brand = models.CharField(max_length=255)
    # processor = models.CharField(max_length=255)
    # ram = models.IntegerField()
    # ssd = models.IntegerField()
    # graphics = models.CharField(max_length=255)
    # screen = models.IntegerField()
    # resolution = models.CharField(max_length=255)
    # nocores = models.IntegerField()
    # nothreads = models.IntegerField()
    # specscore = models.IntegerField()
    # price = models.IntegerField()
    # imageurl = models.CharField(max_length=255)