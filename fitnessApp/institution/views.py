from django.shortcuts import render,HttpResponse,get_object_or_404 
from . import serializers
from .models import Institution
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    return render(request,'institution/index.html')

def add_institution(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            location = request.POST['location']
            category = request.POST['category']
            institution = Institution.objects.create(name=name,location=location,category=category)
            institution.save()
            return HttpResponseRedirect(reverse("institution:detail", args=(institution.id,)))

    except Exception as e:
        print e
    raise Http404("Institution Not Added Successfully")

class RetrieveInstitutionView(generic.DetailView):
    model = Institution
    template_name = 'institution/view_institution.html'

class DetailInstitutionView(generic.DetailView):
    model = Institution
    template_name = 'institution/detail_institution.html'

class EditInstitutionView(generic.DetailView):
    model = Institution
    template_name = 'institution/edit_institution.html'


def update_institution(request,institution_id):
    
    name = request.POST['name']
    location = request.POST['location']
    category = request.POST['category'] 

    institution = get_object_or_404(Institution,pk=institution_id)
    institution.name = name
    institution.location = location
    institution.category = category
    institution.status = 1
    institution.save()

    return HttpResponseRedirect(reverse('institution:detail',args=(institution.id,)))

def delete_institution(request,institution_id):
    institution = get_object_or_404(Institution,pk=institution_id)
    institution.status = 2
    institution.save()

    return HttpResponseRedirect(reverse('institution:detail',args=(institution.id,)))

