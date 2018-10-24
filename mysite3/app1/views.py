from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.forms import FormIn

from .models import Airport
# Create your views here.
def index(request):
    if request.method=='GET':
        form = FormIn()
        return render(request,'mysite3/index1.html',{'form':form})
    if request.method=='POST':
        form = FormIn(request.POST)
        return redirect('mysite3/details.html',{'form':form})
def details(request):
    return render(request,'mysite3/details.html')
def forms(request):
    return render(request,'mysite3/forms.html')
def finalpage(request):
    return render(request,'mysite3/finalpage.html')

import MySQLdb

def list(request):
    db = MySQLdb.connect(user='root', db='A',  passwd='rizwan1998', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Aircraft')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'list.html', {'names': names})
