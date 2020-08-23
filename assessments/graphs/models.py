from django.db import models
import datetime 
import calendar
map_calendar = {v: k for k,v in enumerate(calendar.month_abbr)}
# Create your models here.

class CarsModel(models.Model):

    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    sales = models.PositiveIntegerField()
    resale_value = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    engine_size = models.FloatField()
    horsepower = models.SmallIntegerField()
    wheelbase = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    curb_weight = models.FloatField()
    fuel_capacity = models.FloatField()
    fuel_efficiency = models.SmallIntegerField()
    latest_launch = models.DateField()

    def save(self, *args, **kwargs):
        # date reformat add

        date = self.latest_launch.split("-")
        day = int(date[0])
        month = map_calendar[date[1]]
        year = int("20"+date[2])
        self.latest_launch = datetime.date(year, month, day) 

        super(CarsModel, self).save(*args, **kwargs)


    @staticmethod
    def source():

        return 'cars.csv'

class CVSSVendor(models.Model):

    vendor = models.CharField(max_length=100)
    nr_total_vuln = models.IntegerField()
    nr_total = models.IntegerField()
    weighted_average = models.FloatField()
    percentage_total = models.FloatField()

    @staticmethod
    def source():

        return 'CVSS Score Distribution For Top 50 Vendors By Total Number Of Distinct Vulnerabilities.csv'

class CVSSProduct(models.Model):

    product = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    nr_total_vuln = models.IntegerField(default=0)
    nr_total = models.IntegerField(default=0)
    weighted_average = models.FloatField(default=0)
    percentage_total = models.FloatField(default=0)

    @staticmethod
    def source():

        return 'CVSS Score Distribution For Top 50 Products By Total Number Of Distinct Vulnerabilities.csv'

    
class ProductTop(models.Model):

    product = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100, default="Google")
    product_type = models.CharField(max_length=100)
    nr_total_vuln = models.IntegerField()
    
    @staticmethod
    def source():

        return 'Top 50 Products By Total Number Of Distinct Vulnerabilities .csv'

class VendorTop(models.Model):

    vendor = models.CharField(max_length=100)
    nr_products = models.IntegerField()
    nr_total_vuln = models.IntegerField()
    ratio = models.SmallIntegerField()

    @staticmethod
    def source():

        return 'Top 50 Vendors By Total Number Of Distinct Vulnerabilities .csv'


