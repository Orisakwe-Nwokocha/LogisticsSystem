from django.db import models


from logistics.utility import generate_tracking_number


# Create your models here.

class DeliveryInformation(models.Model):
    sender_name = models.CharField(max_length = 225)
    sender_address = models.CharField(max_length = 225)
    receiver_name = models.CharField(max_length = 225)
    receiver_address = models.CharField(max_length = 225)
    delivery_fee = models.DecimalField(max_digits =100, decimal_places =2)
    delivery_notes = models.TextField()
    DELIVERY_TYPE_CHOICES = (
        ('same day delivery', 'Express'),
        ('next_day_delivery', 'Standard'),
    )
    delivery_type = models.CharField(max_length = 20, choices =DELIVERY_TYPE_CHOICES)
    pickup_address = models.CharField(max_length = 225)
    package = models.TextField()


class Package(models.Model):
    STATUS = [
        ('P', 'PENDING'),
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
    ]
    tracking_number = models.CharField(max_length=15,
                                       unique=True,
                                       default=generate_tracking_number)
    deliveryInformation = models.ForeignKey(DeliveryInformation, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15,
                              choices=STATUS,
                              default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Driver(models.Model):
    pass


class Tracker(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)


class ProgressReport(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE, related_name="progress_reports")





