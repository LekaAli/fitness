from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    render HttpResponse("<h1>Trainer</h1>")