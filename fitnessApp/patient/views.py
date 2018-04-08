from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from . import serializers
from .models import Patient
from django.views import generic
from .serializers import PatientSerializer

patienserializer = PatientSerializer(partial=True)
print patienserializer

# Create your views here.
def index(request):
    
    return render(request,'patient/index.html')

def add_patient(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        idnumber = request.POST['identitynumber']
        province = request.POST['province']
        region = request.POST['region']
        location = request.POST['location']

        patient = Patient.objects.create(
                firstname=firstname,
                lastname=lastname,
                identitynumber=idnumber,
                province=province,
                region=region,
                location=location
            )

        print patient
        patient.save()
        return HttpResponseRedirect(reverse('patient:detail',args=(patient.id,)))

class DetailView(generic.DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'

class UpdateView(generic.DetailView):
    model = Patient
    template_name = 'patient/update_patient.html'

def update_patient(request,patient_id):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        province = request.POST['province']
        region = request.POST['region']
        location = request.POST['location']

        patient = get_object_or_404(Patient,pk=patient_id)
        patient.firstname = firstname
        patient.lastname = lastname
        patient.province = province
        patient.region = region
        patient.location = location
        patient.status = 1
        patient.save()

    return HttpResponseRedirect(reverse('patient:detail',args=(patient_id,)))

def delete_patient(request,patient_id):
    patient = get_object_or_404(Patient,pk=patient_id)
    patient.status = 2
    patient.save()

    return HttpResponseRedirect(reverse('patient:delete_view',args=(patient_id,)))

def delete_view_patient(request,patient_id):
    return render(request,'patient/delete_view_patient.html',{'patient_id':patient_id})

def request_service_patient(request,patient_id):
    """
        patient.id
        service information 
        - health problem
    """
    return HttpResponse("Patient Request service")