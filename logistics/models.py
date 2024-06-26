from django.db import models
from logistics.utility import generate_tracking_number


# Create your models here.

class DeliveryInformation(models.Model):
    sender_name = models.CharField(max_length=225)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=225)
    receiver_address = models.TextField()
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_notes = models.TextField()
    DELIVERY_TYPE_CHOICES = [
        ('E', 'EXPRESS'),
        ('S', 'STANDARD'),
    ]
    delivery_type = models.CharField(max_length=1, choices=DELIVERY_TYPE_CHOICES, default='E')
    pickup_address = models.TextField()


class Package(models.Model):
    STATUS = [
        ('P', 'PENDING'),
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
    ]
    tracking_number = models.CharField(max_length=15, unique=True,
                                       default=generate_tracking_number)
    deliveryInformation = models.ForeignKey(DeliveryInformation, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Driver(models.Model):
    driver_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=11)
    availability = models.BooleanField(default=True)
    driver_address = models.TextField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Tracker(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)


class ProgressReport(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE, related_name="progress_reports")
