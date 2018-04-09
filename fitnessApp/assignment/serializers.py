from rest_framework import serializers
from .models import Assignment
from serviceprovider.models import Serviceprovider

class ServiceProviderSerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField(many=True)
    class Meta:
        model = Serviceprovider
        fields = ('firstname','lastname','category','assignment')