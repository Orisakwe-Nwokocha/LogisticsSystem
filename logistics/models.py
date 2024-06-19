from django.db import models


# Create your models here.


class Package(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=20)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=20)
    receiver_address = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
