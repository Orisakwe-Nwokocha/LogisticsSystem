from rest_framework import serializers
from .models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['tracking_number', 'sender_name',
                  'sender_address', 'receiver_name',
                  'receiver_address', 'weight',
                  'delivery_date', 'status']


