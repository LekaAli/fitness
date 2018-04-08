from django.shortcuts import render
from . import serializers
from .models import Referal
from patient.models import Patient
from serviceProvider.models import Serviceprovider
from institution.models import Institution
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

# Create your views here.
def index(request):
    serviceprovider = Serviceprovider.objects.all()
    patient = Patient.objects.all()
    institution = Institution.objects.all()
    context = {'serviceprovider':serviceprovider,'patient':patient,'institution':institution}
    return render(request,'referal/index.html',context)

def add_referal(request):
    if request.method == "POST":

        patient = request.POST.get("patient")
        patientnames = patient.split(",")
        firstname = patientnames[0]
        lastname = patientnames[1]
        patient = Patient.objects.get(firstname=firstname,lastname=lastname)
        
        serviceprovider = request.POST.get("serviceprovider")
        serviceprovidernames = serviceprovider.split(",")
        firstname = serviceprovidernames[0]
        lastname = serviceprovidernames[1]
        serviceprovider = Serviceprovider.objects.get(firstname=firstname,lastname=lastname)
        
        institution = request.POST.get("institution")
        institution = Institution.objects.get(name=institution)
        
        referal = Referal.objects.create(patient=patient,institution=institution,serviceprovider=serviceprovider)
        referal.save()

    return HttpResponseRedirect(reverse('referal:detail',args=(referal.id,)))

class detail_referal(generic.DetailView):
    model = Referal
    template_name = "referal/referal_detail.html"

def edit_referal(request):
    return HttpResponse("")

def update_referal(request):
    return HttpResponse("")

def check_referal(request):
    return HttpResponse("")
def cancel_referal(request):
    return HttpResponse("")
def accept_referal(request):
    return HttpResponse("")
