from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_safe
from fitnessApp import decode_serializers
from patient import serializers

print decode_serializers.referal()
# print decode_serializers.patient()
# print decode_serializers.serviceProvider()
# print decode_serializers.availability()
# print decode_serializers.institution()


@require_http_methods(["GET"])
def index(request):
    # print "REQUEST: ",request.user
    a = serializers.PatientModule(patient_id="100",patient_name="Leka",patient_surname="Tshoane",patient_health_record="Allergic to cold & other type of foods")
    b = serializers.PatientSerializerModule(a, partial=False)
    from rest_framework.renderers import JSONRenderer
    c = JSONRenderer().render(b.data)
    from django.utils.six import BytesIO
    d = BytesIO(c)
    from rest_framework.parsers import JSONParser
    data = JSONParser().parse(d)
    print data
    b = serializers.PatientSerializerModule(data=data, partial=False)
    b.is_valid(raise_exception=True)

    value =  b.validated_data
    print serializers.PatientSerializerModule
    content = {'value':value}
    return render(request,'html/fitness/index.html',content)

@require_http_methods(["GET"])
def signIn(request):
    return render(request,'html/fitness/sign_in.html')

@require_http_methods(["GET"])
def register(request):
    return render(request,'html/fitness/register.html')

@require_http_methods(["POST"])
def registrationComplete(request):
    return render(request,"html/fitness/registrationComplete.html")

@require_http_methods(["GET","POST"])
def signedIn(request):
    return render(request,"html/fitness/signedIn.html")

@require_http_methods(["GET"])
def notifications(request):
    return render(request,"html/fitness/notifications.html")

@require_http_methods(["GET"])
def referals(request):
    return render(request,"html/fitness/referals.html")
