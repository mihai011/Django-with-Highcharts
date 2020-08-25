from django.db import models
import logging 

import datetime 
import calendar


map_calendar = {v: k for k,v in enumerate(calendar.month_abbr)}
logger = logging.getLogger("app_info")
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

    @classmethod
    def create_data(cls):
        
        col_name = "manufacturer"
        series_name = "number of cars"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])
        # count number of cars for each manufacturer
        values = []
        for s in categories:
            values.append(cls.objects.filter(manufacturer=s).count())

        logger.info("Retrieved data from class:"+str(CarsModel))
        return list(categories), values, col_name, series_name


    def save(self, *args, **kwargs):
        # date reformat add for "latest-launch field"

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

    @classmethod
    def create_data(cls):

        col_name = "vendor"
        series_name = "total vulnerabilities"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])

        # get number of vulnerabilities for each vendor
        values = []
        for s in categories:
            values.append(sum([s.nr_total_vuln for s in cls.objects.filter(vendor=s)]))

        logger.info("Retrieved data from class:"+str(CVSSVendor))
        return list(categories), values, col_name, series_name

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

    @classmethod
    def create_data(cls):

        col_name = "product"
        series_name = "total vulnerabilities"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])

        # get number of vulnerabilities for each vendor
        values = []
        for s in categories:
            values.append(sum([s.nr_total_vuln for s in cls.objects.filter(product=s)]))

        logger.info("Retrieved data from class:"+str(CVSSProduct))
        return list(categories), values, col_name, series_name


    @staticmethod
    def source():

        return 'CVSS Score Distribution For Top 50 Products By Total Number Of Distinct Vulnerabilities.csv'

    
class ProductTop(models.Model):

    product = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100, default="Google")
    product_type = models.CharField(max_length=100)
    nr_total_vuln = models.IntegerField()

    @classmethod
    def create_data(cls):

        col_name = "product"
        series_name = "total vulnerabilities"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])

        # get number of vulnerabilities for each vendor
        values = []
        for s in categories:
            values.append(sum([s.nr_total_vuln for s in cls.objects.filter(product=s)]))

        logger.info("Retrieved data from class:"+str(ProductTop))
        return list(categories), values, col_name, series_name
    
    @staticmethod
    def source():

        return 'Top 50 Products By Total Number Of Distinct Vulnerabilities .csv'

class VendorTop(models.Model):

    vendor = models.CharField(max_length=100)
    nr_products = models.IntegerField()
    nr_total_vuln = models.IntegerField()
    ratio = models.SmallIntegerField()

    @classmethod
    def create_data(cls):

        col_name = "vendor"
        series_name = "total vulnerabilities"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])

        # get number of vulnerabilities for each vendor
        values = []
        for s in categories:
            values.append(sum([s.nr_total_vuln for s in cls.objects.filter(vendor=s)]))

        logger.info("Retrieved data from class:"+str(VendorTop))
        return list(categories), values, col_name, series_name


    @staticmethod
    def source():

        return 'Top 50 Vendors By Total Number Of Distinct Vulnerabilities .csv'

class VulnTrends(models.Model):

    year = models.SmallIntegerField()
    nr_vuln = models.SmallIntegerField()
    dos = models.SmallIntegerField()
    code_exec = models.SmallIntegerField()
    overflow = models.SmallIntegerField()
    memory_cor = models.SmallIntegerField()
    sql_injection = models.SmallIntegerField()
    xss = models.SmallIntegerField()
    Directory = models.SmallIntegerField()
    http_resp = models.SmallIntegerField()
    bypass = models.SmallIntegerField()
    gain_info = models.SmallIntegerField()
    gain_priv = models.SmallIntegerField()
    csrf = models.SmallIntegerField()
    exploits = models.SmallIntegerField()


    @classmethod
    def create_data(cls):

        col_name = "year"
        series_name = "total vulnerabilities"

        categories = set([f[col_name] for f in list(cls.objects.values(col_name))])

        # get number of vulnerabilities for each vendor
        values = []
        for s in categories:
            values.append(sum([s.nr_vuln for s in cls.objects.filter(year=s)]))

        logger.info("Retrieved data from class:"+str(VulnTrends))
        return list(categories), values, col_name, series_name


    @staticmethod
    def source():

        return "Vulnerability Trends Over Time .csv"


