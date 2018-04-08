from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from rest_framework import serializers

class ReferalModule(object):

    def __init__(self,referal_id,referal_date,referal_time,referal_comment,patient_id,sp_identity_key,institution_identity_key):
        from datetime import datetime

        self.referal_id = referal_id
        self.referal_date = referal_date or datetime.date(datetime.now())
        self.referal_time = referal_time or datetime.time(datetime.now())
        self.referal_comment = referal_comment
        self.patient_id = patient_id
        self.sp_identity_key = sp_identity_key
        self.institution_identity_key = institution_identity_key
        
class ReferalSerializerModule(serializers.Serializer):

    referal_id = serializers.CharField(max_length=8)
    referal_date = serializers.DateField()
    referal_time = serializers.TimeField()
    referal_comment = serializers.CharField(max_length=300)
    patient_id = serializers.CharField(max_length=8)
    sp_identity_key = serializers.CharField(max_length=8)
    institution_identity_key = serializers.CharField(max_length=8)

    def create(self,validated_data):
        return ReferalModule(**validated_data)

    def update(self,instance,validated_data):
        instance.referal_id = validated_data.get('referal_id',instance.referal_id)
        instance.referal_date = validated_data.get('referal_date',instance.referal_date)
        instance.referal_time = validated_data.get('referal_time', instance.referal_time)
        instance.referal_comment = validated_data.get('referal_comment',instance.referal_comment)
        instance.patient_id = validated_data.get('patient_id',instance.patient_id)
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        return instance