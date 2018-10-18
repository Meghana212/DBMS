from django.shortcuts import render
from django.http import HttpResponse

from .models import Airport
# Create your views here.

def index(request):
    data = Airport.objects.all()
    return render(request,'mysite3/index.html',{'data':data})
def details(request):
    return render(request,'mysite3/details.html')
def forms(request):
    return render(request,'mysite3/forms.html')
def finalpage(request):
    return render(request,'mysite3/finalpage.html')
