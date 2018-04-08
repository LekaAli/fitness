from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.utils.six import BytesIO
from fitnessApp import serializers

def referal():

    referal = serializers.Referal(referal_id="100",referal_date="2017-06-22",referal_time="15:38:05",referal_comment="Comment about the patient referal_comment",patient_id="100",sp_identity_key="200",institution_identity_key="500")
    #Serializer instance with None attribute values, since no initial object is passed to it.
    serializer = serializers.ReferalSerializer(partial=False) 
    print serializer.data

    # No partial update partial set to False
    # Serialize the referal class instance
    serializer = serializers.ReferalSerializer(referal,partial=False)
    print serializer.data

    # Render the data into json
    from rest_framework.renderers import JSONRenderer
    json = JSONRenderer().render(serializer.data)

    # Deserialize the json object
    # by parsing a stream into Python native datatypes
    from django.utils.six import BytesIO
    from rest_framework.parsers import JSONParser
    stream = BytesIO(json)
    data = JSONParser().parse(stream)

    # Restore the native datatypes into a dictionary of validated data
    serializer = serializers.ReferalSerializer(data=data,partial=False)
    # returns a 404 response if the data was invalid
    if not serializer.is_valid(raise_exception=False):
        raise Exception("Invalid Data Structure")

    
    referalInstance = serializers.ReferalSerializer().create(serializer.validated_data)
    print "++: ",referalInstance.referal_comment
    serializer = serializers.ReferalSerializer().update(referalInstance,serializer.validated_data)
    print "==: ",serializer.referal_comment
    return serializer

def patient():
    
    patient = serializers.Patient(patient_id="100",patient_name="Leka",patient_surname="Tshoane",patient_health_record="Allergic to cold & other type of foods")
    serializer = serializers.PatientSerializer(patient)

    json = JSONRenderer().render(serializer.data)

    stream = BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = serializers.PatientSerializer(data=data)
    if not serializer.is_valid(raise_exception=True):
        raise Exception("Invalid Data Structure")
    patientInstance = serializers.PatientSerializer().create(serializer.validated_data)
    serializer = serializers.PatientSerializer().update(patientInstance,serializer.validated_data)
    return serializer

def availability():
    
    availability = serializers.Availability(sp_identity_key="200",availabilty_s_date="2017-06-19",availabilty_e_date="2017-06-23",availabilty_s_time="09:00",availabilty_e_time="17:30")
    serializer = serializers.AvailabilitySerializer(availability)

    json = JSONRenderer().render(serializer.data)

    stream = BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = serializers.AvailabilitySerializer(data=data)
    if not serializer.is_valid(raise_exception=True):
        raise Exception("Invalid Data Structure")
    availabilityInstance = serializers.AvailabilitySerializer().create(serializer.validated_data)
    serializer = serializers.AvailabilitySerializer().update(availabilityInstance,serializer.validated_data)
    return serializer

def institution():
    
    institution = serializers.Institution(institution_identity_key="500",institution_name="Tshoane Fitness Center",institution_type="Fitness Center",institution_location="Pretoria CBD")
    serializer = serializers.InstitutionSerializer(institution)

    json = JSONRenderer().render(serializer.data)

    stream = BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = serializers.InstitutionSerializer(data=data)
    if not serializer.is_valid(raise_exception=True):
        raise Exception("Invalid Data Structure")
    institutionInstance = serializers.InstitutionSerializer().create(serializer.validated_data)
    serializer = serializers.InstitutionSerializer().update(institutionInstance,serializer.validated_data)
    return serializer

def serviceProvider():

    serviceProvider = serializers.ServiceProvider(sp_identity_key="200",sp_name="Alfred",sp_surname="Tshoane",sp_type="Doctor",institution_identity_key="500")
    serializer = serializers.ServiceProviderSerializer(serviceProvider)

    json = JSONRenderer().render(serializer.data)

    stream = BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = serializers.ServiceProviderSerializer(data=data)
    if not serializer.is_valid(raise_exception=True):
        raise Exception("Invalid Data Structure")
    serviceInstance = serializers.ServiceProviderSerializer().create(serializer.validated_data)
    serializer = serializers.ServiceProviderSerializer().update(serviceInstance,serializer.validated_data)
    return serializer
    
