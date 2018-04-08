from rest_framework import serializers
from .models import Assignment
from serviceProvider.models import Serviceprovider

class ServiceProviderSerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField(many=True)
    class Meta:
        model = Serviceprovider
        fields = ('firstname','lastname','category','assignment')