from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework import serializers


class AvailabilityModule(serializers.Serializer):
    
    def __init__(self, sp_identity_key,availabilty_s_date,availabilty_e_date,availabilty_s_time,availabilty_e_time):
        self.sp_identity_key = sp_identity_key
        self.availabilty_s_date  = availabilty_s_date
        self.availabilty_e_date = availabilty_e_date
        self.availabilty_s_time = availabilty_s_time
        self.availabilty_e_time = availabilty_e_time
        
class AvailabilitySerializerModule(serializers.Serializer):

    sp_identity_key = serializers.CharField(max_length=8)
    availabilty_s_date = serializers.DateField()
    availabilty_e_date = serializers.DateField()
    availabilty_s_time = serializers.TimeField()
    availabilty_e_time = serializers.TimeField()

    def create(self,validated_data):
        return AvailabilityModule(**validated_data)

    def update(self,instance,validated_data):
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.availabilty_s_date = validated_data.get('availabilty_s_date',instance.availabilty_s_date)
        instance.availabilty_e_date = validated_data.get('availabilty_e_date',instance.availabilty_e_date)
        instance.availabilty_s_time = validated_data.get('availabilty_s_time',instance.availabilty_s_time)
        instance.availabilty_e_time = validated_data.get('availabilty_e_time',instance.availabilty_e_time)
        return instance