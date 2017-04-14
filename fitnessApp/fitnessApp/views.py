from django.shortcuts import render,HttpResponse

def index(request):
    
    return render(request,'html/fitness/index.html')

def signIn(request):

    return render(request,'html/fitness/sign_in.html')

def register(request):

    return render(request,'html/fitness/register.html')
