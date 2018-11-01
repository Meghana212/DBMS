from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.forms import FormIn
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Airport,Passenger
from django.db import connection
pi = 1
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
        return render(request,'mysite3/index1.html',{'data':data})
    if request.method=='POST':
        cursor = connection.cursor()
        fro = request.POST.get('from')
        to = request.POST.get('to')
        cursor.execute("SELECT ap_id from airport where city=%s",[fro])
        s1 = cursor.fetchall()
        s = s1[0]
        cursor.execute("SELECT ap_id from airport where city=%s",[to])
        d1 = cursor.fetchone()
        d = d1[0]
        depart = request.POST.get('depart')
        #arrival = request.POST.get('arrival')
        depart = str(depart)
        depart = depart + '%'
        cursor.execute("SELECT Class,Fare,Departure from fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and fs.Departure like %s",[s,d,depart])
        avf = cursor.fetchall()
        connection.close()
        return render(request,'mysite3/details.html',{'avf':avf})
    else:
        data = Airport.objects.all()
        return render(request,'mysite3/index1.html',{'data':data})


'''def details(request):
    return render(request,'mysite3/details.html')'''
def forms(request):
    if request.method=='GET':
        return render(request,'mysite3/forms.html')
    if request.method=='POST':
        fname = request.POST.get('first_name')
        mname = request.POST.get('middle_name')
        lname = request.POST.get('last_name')
        em = request.POST.get('EMAIL')
        global pi
        p1 = Passenger(p_id=pi,firstname=fname,middlename=mname,lastname=lname,email=em)
        p1.save()
        pi =pi+1
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
