from django.contrib import admin

from logistics.models import Package, DeliveryInformation


# Register your models here.

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'weight', 'deliveryInformation', 'delivery_date', 'status', 'created_at']
    list_per_page = 10
    search_fields = ['tracking_number', 'weight', 'deliveryInformation', 'delivery_date', 'status', 'created_at']
    list_editable = ['delivery_date', 'status', 'deliveryInformation']


@admin.register(DeliveryInformation)
class DeliveryInformationAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'receiver_name', 'receiver_address', 'delivery_type']
    list_per_page = 10
    search_fields = ['sender_name', 'receiver_name', 'receiver_address', 'delivery_type']
    list_editable = ['receiver_name', 'receiver_address', 'delivery_type']
