from django.db import models


# Create your models here.


class Package(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=20)
    sender_address = models.TextField()



class Driver:
    pass


class ProgressReport(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)


class Tracker(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    progress_reports = models.ManyToManyField(ProgressReport)
