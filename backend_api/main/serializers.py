from rest_framework import serializers
from . import models

class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['user', 'address']
        