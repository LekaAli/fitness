from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . import serializers
from .models import Person
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'serviceprovider/index.html')

def add_service_provider(request):
    try:
        if request.method == "POST":
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            category = request.POST['category']
            qualification = request.POST['qualification']
            speciality = request.POST['speciality']
            service_provider = Person.objects.create(firstname=firstname,lastname=lastname,category=category,qualification=qualification,speciality=speciality)
            service_provider.save() 
    except:
        raise Http404("Error adding service provider")
    return HttpResponseRedirect(reverse('serviceprovider:detail',args=(service_provider.id,)))

class DetailInstitutionView(generic.DetailView):
    model = Person
    template_name = 'serviceprovider/detail_serviceprovider.html'

def update_service_provider(request,service_provider_id):
    
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        category = request.POST['category']
        qualification = request.POST['qualification']
        speciality = request.POST['speciality']
    
        serviceprovider = get_object_or_404(Serviceprovider,pk=service_provider_id)
        serviceprovider.firstname = firstname
        serviceprovider.lastname = lastname
        serviceprovider.category = category
        serviceprovider.qualification = qualification
        serviceprovider.speciality = speciality
        serviceprovider.status = 2
        serviceprovider.save()

    return HttpResponseRedirect(reverse('serviceprovider:detail',args=(serviceprovider.id,)))

def delete_service_provider(request,service_provider_id):
    serviceprovider = get_object_or_404(Person,pk=service_provider_id)
    serviceprovider.status = 3
    serviceprovider.save()
    return HttpResponseRedirect(reverse('serviceprovider:detail',args=(serviceprovider.id,)))

class RetrieveServiceProviderView(generic.DetailView):
    model = Person
    template_name = 'serviceprovider/retrieve_serviceprovider.html'

class EditServiceProviderView(generic.DetailView):
    model = Person
    template_name = 'serviceprovider/edit_serviceprovider.html'
