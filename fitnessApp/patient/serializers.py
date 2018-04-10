from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework import serializers
from .models import Patient
# from referal.models import Referal

class PatientModule(object):
    
    def __init__(self,patient_id,patient_name,patient_surname,patient_health_record):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_surname = patient_surname
        self.patient_health_record = patient_health_record
        
class PatientSerializerModule(serializers.Serializer):
    
    patient_id = serializers.CharField(max_length=8)
    patient_name = serializers.CharField(max_length=200)
    patient_surname = serializers.CharField(max_length=200)
    patient_health_record = serializers.CharField(max_length=300)

    def create(self,validated_data):
        return PatientModule(**validated_data)

    def update(self,instance,validated_data):
        instance.patient_id = validated_data.get('patient_id',instance.patient_id)
        instance.patient_name = validated_data.get('patient_name',instance.patient_name)
        instance.patient_surname = validated_data.get('',instance.patient_surname)
        instance.patient_health_record = validated_data.get('patient_health_record',instance.patient_health_record)
        return instance

# class PatientSerializer(serializers.ModelSerializer):
#     referal = serializers.StringRelatedField()
#     institution = serializers.StringRelatedField()
#     serviceprovider = serializers.StringRelatedField()
#     class Meta:
#         model = Patient
#         fields = ('firstname','lastname','referal','institution','serviceprovider')

