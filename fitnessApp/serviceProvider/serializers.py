from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework import serializers

class ServiceProviderModule(serializers.Serializer):
    
    def __init__(self,sp_identity_key,sp_name,sp_surname,sp_type,institution_identity_key):
        self.sp_identity_key = sp_identity_key
        self.sp_name = sp_name
        self.sp_surname = sp_surname
        self.sp_type = sp_type
        self.institution_identity_key = institution_identity_key

class ServiceProviderSerializerModule(serializers.Serializer):

    sp_identity_key = serializers.CharField(max_length=8)
    sp_name = serializers.CharField(max_length=200)
    sp_surname = serializers.CharField(max_length=200)
    sp_type = serializers.CharField(max_length=25)
    institution_identity_key = serializers.CharField(max_length=8)

    def create(self,validated_data):
        return ServiceProviderModule(**validated_data)

    def update(self,instance,validated_data):
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.sp_name = validated_data.get('sp_name',instance.sp_name)
        instance.sp_surname = validated_data.get('sp_surname',instance.sp_surname)
        instance.sp_type = validated_data.get('sp_type',instance.sp_type)
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        return instance