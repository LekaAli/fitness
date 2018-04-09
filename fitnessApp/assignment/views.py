from django.shortcuts import render,get_object_or_404,HttpResponse
from serviceprovider.models import Serviceprovider
from institution.models import Institution
from .models import Assignment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views import View
from .serializers import ServiceProviderSerializer

# Create your views here.
print ServiceProviderSerializer()

def index(request):
    institution = Institution.objects.all()
    serviceprovider = Serviceprovider.objects.all()

    return render(request,
        'assignment/index.html',
        {'institution':institution,
        'serviceprovider':serviceprovider
        })

def add_assignment(request):
    if request.method == 'POST':
        serviceprovider = request.POST['serviceprovider']
        institution = request.POST['institution']

        attrValueChunks = serviceprovider.split(',')
        firstname = attrValueChunks[0]
        lastname = attrValueChunks[1]

        serviceprovider = Serviceprovider.objects.get(firstname=firstname.strip(),lastname=lastname.strip())
        institution = Institution.objects.get(name=institution.strip())
    
        assignment = Assignment(serviceprovider=serviceprovider,institution=institution,status=0)
        assignment.save()

        return HttpResponseRedirect(reverse('assignment:detail',args=(assignment.id,)))

def update_assignment(request,assignment_id):
    if request.method == 'POST':
        serviceprovider = request.POST['serviceprovider']
        print request.POST
        institution = request.POST['institution']

        attrValueChunks = serviceprovider.split(',')
        firstname = attrValueChunks[0]
        lastname = attrValueChunks[1]

        serviceprovider = Serviceprovider.objects.get(firstname=firstname.strip(),lastname=lastname.strip())
        institution = Institution.objects.get(name=institution.strip())

        assignment = Assignment.objects.get(pk=assignment_id)
        assignment.serviceprovider = serviceprovider
        assignment.institution = institution
        assignment.save()

        return HttpResponseRedirect(reverse('assignment:detail',args=(assignment.id,)))


def delete_assignment(request,serviceprovider_id):
    pass

class RetrieveAssignentView(generic.DetailView):
    model = Assignment
    template_name = 'assignment/view_assignment.html'


class EditAssignentView(View):
    
    template_name = 'assignment/edit_assignment.html'

    def post(self,request,*args,**kwargs):
        assignment_id = kwargs.get('pk')

        assignment = Assignment.objects.get(id=assignment_id)
        institution = Institution.objects.all()
        serviceprovider = Serviceprovider.objects.all()
        context = {'serviceprovider':serviceprovider,'institution':institution,'assignment':assignment}
        return render(request.self.template_name,context)

    def get(self,request,*args,**kwargs):
        assignment_id = kwargs.get('pk')
        assignment = Assignment.objects.get(id=assignment_id)
        institution = Institution.objects.all()
        serviceprovider = Serviceprovider.objects.all()
        context = {'serviceprovider':serviceprovider,'institution':institution,'assignment':assignment}
        return render(request,self.template_name,context)

class UpdateAssignmentView(generic.DetailView):
    model = Assignment
    template_name = 'assignment/update_assignment.html'

class DetailAssignmentView(generic.DetailView):
    model = Assignment
    template_name = 'assignment/detail_assignment.html'

