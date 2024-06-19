from django.db import models


# Create your models here.


class Package(models.Model):
    STATUS = [
        ('P', 'PENDING'),
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
    ]
    tracking_number = models.CharField(max_length=15,
                                       unique=True,
                                       default=generate_tracking_number)

    DeliveryInformation = models.ForeignKey(DeliveryInformation, on_delete=models.CASCADE)

    weight = models.DecimalField(max_digits=10,
                                 decimal_places=2)
    delivery_date = models.DateField(null=True,
                                     blank=True)
    status = models.CharField(max_length=50,
                              choices=STATUS,
                              default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Driver:
    pass


class DeliveryInformation(models.Model):
    sender_name = models.CharField(max_length=20)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=20)
    receiver_address = models.TextField()


class ProgressReport(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)


class Tracker(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    progress_reports = models.ManyToManyField(ProgressReport)
