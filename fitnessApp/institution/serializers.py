from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework import serializers

class InstitutionModule(object):
    
    def __init__(self,institution_identity_key,institution_name,institution_type,institution_location):
        self.institution_identity_key = institution_identity_key
        self.institution_name = institution_name
        self.institution_type = institution_type
        self.institution_location = institution_location
        
class InstitutionSerializerModule(serializers.Serializer):

    institution_identity_key = serializers.CharField(max_length=8)
    institution_name = serializers.CharField(max_length=200)
    institution_type = serializers.CharField(max_length=25)
    institution_location = serializers.CharField(max_length=200)

    def create(self,validated_data):
        return InstitutionModule(**validated_data)

    def update(self,instance,validated_data):
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        instance.institution_name = validated_data.get('institution_name',instance.institution_name)
        instance.institution_type = validated_data.get('institution_type',instance.institution_type)
        instance.institution_location = validated_data.get('institution_location',instance.institution_location)
        return instance