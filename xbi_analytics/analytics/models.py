from django.db import models

class GraphData(models.Model):
    date = models.DateField()
    month = models.CharField(max_length=12)
    rate = models.IntegerField()

class GridData(models.Model):
    group = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    sending_city = models.CharField(max_length=30)
    receiving_city = models.CharField(max_length=30)

class PieChartData(models.Model):
    group = models.CharField(max_length=10)
    fraction = models.IntegerField()
