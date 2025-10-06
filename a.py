import csv

class Laptop:
    def __init__(self, laptop):
        self.model_name = laptop
        self.brand = ""
        self.processor_name = ""
        self.ram = ""
        self.ssd = ""
        self.hard_disk = ""
        self.operating_system = ""
        self.graphics = ""
        self.screen_size = ""
        self.resolution = ""
        self.n_oc = ""
        self.n_ot = ""
        self.sc = ""
        self.price = ""
        
with open('/data/laptop.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    print(rows[0])
