from rest_framework import serializers

class Institution(serializers.Serializer):
    
    def __init__(self,institution_identity_key,institution_name,institution_type,institution_location):
        self.institution_identity_key = institution_identity_key
        self.institution_name = institution_name
        self.institution_type = institution_type
        self.institution_location = institution_location

class ServiceProvider(serializers.Serializer):
    
    def __init__(self,sp_identity_key,sp_name,sp_surname,sp_type,institution_identity_key):
        self.sp_identity_key = sp_identity_key
        self.sp_name = sp_name
        self.sp_surname = sp_surname
        self.sp_type = sp_type
        self.institution_identity_key = institution_identity_key
        

class Patient(serializers.Serializer):
    
    def __init__(self,patient_id,patient_name,patient_surname,patient_health_record):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_surname = patient_surname
        self.patient_health_record = patient_health_record

class Referal(serializers.Serializer):

    def __init__(self,referal_id,referal_date,referal_time,referal_comment,patient_id,sp_identity_key,institution_identity_key):
        from datetime import datetime

        self.referal_id = referal_id
        self.referal_date = referal_date or datetime.date(datetime.now())
        self.referal_time = referal_time or datetime.time(datetime.now())
        self.referal_comment = referal_comment
        self.patient_id = patient_id
        self.sp_identity_key = sp_identity_key
        self.institution_identity_key = institution_identity_key
        
class Availability(serializers.Serializer):
    
    def __init__(self, sp_identity_key,availabilty_s_date,availabilty_e_date,availabilty_s_time,availabilty_e_time):
        self.sp_identity_key = sp_identity_key
        self.availabilty_s_date  = availabilty_s_date
        self.availabilty_e_date = availabilty_e_date
        self.availabilty_s_time = availabilty_s_time
        self.availabilty_e_time = availabilty_e_time


class AvailabilitySerializer(serializers.Serializer):

    sp_identity_key = serializers.CharField(max_length=8)
    availabilty_s_date = serializers.DateField()
    availabilty_e_date = serializers.DateField()
    availabilty_s_time = serializers.TimeField()
    availabilty_e_time = serializers.TimeField()

    def create(self,validated_data):
        return Availability(**validated_data)

    def update(self,instance,validated_data):
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.availabilty_s_date = validated_data.get('availabilty_s_date',instance.availabilty_s_date)
        instance.availabilty_e_date = validated_data.get('availabilty_e_date',instance.availabilty_e_date)
        instance.availabilty_s_time = validated_data.get('availabilty_s_time',instance.availabilty_s_time)
        instance.availabilty_e_time = validated_data.get('availabilty_e_time',instance.availabilty_e_time)
        return instance


class InstitutionSerializer(serializers.Serializer):

    institution_identity_key = serializers.CharField(max_length=8)
    institution_name = serializers.CharField(max_length=200)
    institution_type = serializers.CharField(max_length=25)
    institution_location = serializers.CharField(max_length=200)

    def create(self,validated_data):
        return Institution(**validated_data)

    def update(self,instance,validated_data):
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        instance.institution_name = validated_data.get('institution_name',instance.institution_name)
        instance.institution_type = validated_data.get('institution_type',instance.institution_type)
        instance.institution_location = validated_data.get('institution_location',instance.institution_location)
        return instance


class ServiceProviderSerializer(serializers.Serializer):

    sp_identity_key = serializers.CharField(max_length=8)
    sp_name = serializers.CharField(max_length=200)
    sp_surname = serializers.CharField(max_length=200)
    sp_type = serializers.CharField(max_length=25)
    institution_identity_key = serializers.CharField(max_length=8)

    def create(self,validated_data):
        return ServiceProvider(**validated_data)

    def update(self,instance,validated_data):
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.sp_name = validated_data.get('sp_name',instance.sp_name)
        instance.sp_surname = validated_data.get('sp_surname',instance.sp_surname)
        instance.sp_type = validated_data.get('sp_type',instance.sp_type)
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        return instance


class PatientSerializer(serializers.Serializer):
    
    patient_id = serializers.CharField(max_length=8)
    patient_name = serializers.CharField(max_length=200)
    patient_surname = serializers.CharField(max_length=200)
    patient_health_record = serializers.CharField(max_length=300)

    def create(self,validated_data):
        return Patient(**validated_data)

    def update(self,instance,validated_data):
        instance.patient_id = validated_data.get('patient_id',instance.patient_id)
        instance.patient_name = validated_data.get('patient_name',instance.patient_name)
        instance.patient_surname = validated_data.get('',instance.patient_surname)
        instance.patient_health_record = validated_data.get('patient_health_record',instance.patient_health_record)
        return instance


def validate_referal_comment(value):
        if not value:
            raise serializers.ValidationError("referal Comment Required.")
        return value


class ReferalSerializer(serializers.Serializer):

    referal_id = serializers.CharField(max_length=8)
    referal_date = serializers.DateField()
    referal_time = serializers.TimeField()
    referal_comment = serializers.CharField(max_length=300)
    # referal_comment = serializers.CharField(max_length=300,validators=[validate_referal_comment])
    patient_id = serializers.CharField(max_length=8)
    sp_identity_key = serializers.CharField(max_length=8)
    institution_identity_key = serializers.CharField(max_length=8)

    def validate_referal_comment(self,value):
        if not value:
            raise serializers.ValidationError("referal Comment Required.")
        return value

    def create(self,validated_data):
        return Referal(**validated_data)

    def update(self,instance,validated_data):
        instance.referal_id = validated_data.get('referal_id',instance.referal_id)
        instance.referal_date = validated_data.get('referal_date',instance.referal_date)
        instance.referal_time = validated_data.get('referal_time', instance.referal_time)
        instance.referal_comment = validated_data.get('referal_comment',instance.referal_comment)
        instance.patient_id = validated_data.get('patient_id',instance.patient_id)
        instance.sp_identity_key = validated_data.get('sp_identity_key',instance.sp_identity_key)
        instance.institution_identity_key = validated_data.get('institution_identity_key',instance.institution_identity_key)
        return instance
