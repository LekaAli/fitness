from django.shortcuts import render
from . import serializers
from .models import Availability
from institution.models import Institution
from serviceprovider.models import Serviceprovider
from django.urls import reverse
from django.views import generic
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    institution = Institution.objects.all()
    serviceprovider = Serviceprovider.objects.all()
    availability = Availability.objects.all()
    context = {'institutions': institution,'serviceproviders':serviceprovider,'availability':availability}
    return render(request,'availability/index.html',context)

def edit_availability(request,availability_id):

    institution = Institution.objects.all()
    serviceprovider = Serviceprovider.objects.all()
    availability = Availability.objects.get(pk=availability_id)
    context = {'institution':institution,'serviceprovider':serviceprovider,'availability':availability}
    return render(request,'availability/availability_edit.html',context)

class AddAvailabilityView(View):
    
    template_name = 'availability/availability_add.html'

    def get(self,request,*agrs,**kwargs):
        return HttpResponse("")

    def post(self,request,*agrs,**kwargs):
        print request.POST
        status = 0
        serviceprovider = request.POST.get('serviceprovider')
        institution = request.POST.get('institution')
        availability = request.POST.get('availability')
        starttime  = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        institution = Institution.objects.get(name=institution)
        serviceprovidernames = serviceprovider.split(',')
        firstname = serviceprovidernames[0]
        lastname = serviceprovidernames[1] 
        serviceprovider = Serviceprovider.objects.get(firstname=firstname,lastname=lastname)
        
        if availability != "Weekly":
            availability = Availability(
                status=status,
                serviceprovider=serviceprovider,
                institution=institution,
                daily=availability,
                starttime=starttime,
                endtime=endtime)
            availability.save()
        else:
            availability = Availability(
                status=status,
                serviceprovider=serviceprovider,
                institution=institution,
                Weekly=availability,
                starttime=starttime,
                endtime=endtime)
            availability.save()

        return HttpResponseRedirect(reverse('availability:detail',args=(availability.id,)))


class DetailAvailabilityView(generic.DetailView):
    model = Availability
    template_name = 'availability/availability_detail.html'

def update_availability(request,availability_id):
    daily=5
    weekly = False
    if request.method == "POST":
        status = request.POST.get("status")
        avail = request.POST.get("availability")    
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        institution = request.POST.get("institution")
        serviceprovider = request.POST.get("serviceprovider")
        nameChunks = serviceprovider.split(",")
        firstname = nameChunks[0]
        lastname = nameChunks[1]

        serviceprovider = Serviceprovider.objects.get(firstname=firstname,lastname=lastname)
        institution = Institution.objects.get(name=institution)
        availability = Availability.objects.get(pk=availability_id)

        availability.firstname = firstname
        availability.lastname = lastname
        availability.status = status
        if avail == "weekly":
            availability.weekly = True
        else:
            daily = avail
            availability.daily = avail
        availability.starttime = starttime
        availability.endtime = endtime
        availability.serviceprovider = serviceprovider
        availability.institution = institution
        availability.save()

    return HttpResponseRedirect(reverse("availability:detail",args=(availability.id,)))


def check_availability(request,service_provider_id):
    pass

def delete_availability(request,service_provider_id):
    pass
