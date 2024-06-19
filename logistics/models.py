from django.db import models


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




