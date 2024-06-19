from rest_framework import serializers
from .models import Package
from django.contrib.auth.models import User


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['tracking_number', 'weight',
                  'delivery_date', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
