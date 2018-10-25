from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.forms import FormIn
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Airport
from django.db import connections

# Create your views here.
'''def index(request):
    data = Airport.objects.all()
    #if request.method=='GET':
        #form = FormIn()
    return render(request,'mysite3/index1.html',{'data':data})
    #if request.method=='POST':
        #form = FormIn(request.POST)
        #return redirect('mysite3/details.html',{'form':form})'''
def index(request):
    if request.method=='GET':
        data = Airport.objects.all()
        return render(request,'mysite3/index.html',{'data':data})
    if request.method=='POST':
        fro = request.POST.get('From')
        to = request.POST.get('To')
        depart = request.POST.get('depart')
        arrival = request.POST.get('arrival')

        cursor = connection.cursor()
        cursor.execute("SELECT Class,Fare,Departure from fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.R_ID and f.R_id = fs.R_ID and fs.Departure like '2018-10-18%'"[fro,to])
        names = cursor.fetchall()
        db.close()
        return redirect(request,'mysite3/details.html',{'names': names})
    else:
        data = Airport.objects.all()
        return render(request,'mysite3/index.html',{'data':data})


'''def details(request):
    return render(request,'mysite3/details.html')'''
def forms(request):
    return render(request,'mysite3/forms.html')
def finalpage(request):
    return render(request,'mysite3/finalpage.html')

import MySQLdb

#def list(request):
#    db = MySQLdb.connect(user='root', db='A',  passwd='rizwan1998', host='localhost')
#    cursor = db.cursor()wwwwwwwwwwww
#    cursor.execute('SELECT * FROM Aircraft')
#    names = [row[0] for row in cursor.fetchall()]
#    db.close()i
#    return render(request, 'list.html', {'names': names})

'''class AirportCreateView(CreateView):
    model = Airport
    fields = ('city')
    success_url = reverse_lazy('person_changelist')'''
