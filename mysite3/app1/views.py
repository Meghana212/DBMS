from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.forms import FormIn
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Airport,Passenger,BookingDetails,Fare,FlightSchedule,Discounts
from django.db import connection
from django.template import Context, Template
FlightID =1
FareID=1
Bookingdate =""
Totalcost=1
PayerID=0
Ph_no=0
totalcost=0
import datetime
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
    elif request.method=='POST':
        cursor = connection.cursor()
        fro = request.POST.get('from')
        to = request.POST.get('to')
        NOP = request.POST.get('NOP')
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
        e = "Economy%"
        b = "Business%"
        f = "First%"
        res_count=cursor.execute("SELECT A_Number,Class,Fare,Departure,Economy_RCapacity 'Available seats',FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and Economy_RCapacity>=%s UNION SELECT A_Number,Class,Fare,Departure,BusinessClass_RCapacity,FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and BusinessClass_RCapacity>=%s UNION SELECT A_Number,Class,Fare,Departure,FirstClass_RCapacity,FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and FirstClass_RCapacity>=%s",[s,d,depart,e,NOP,s,d,depart,b,NOP,s,d,depart,f,NOP]);
        #res_count=cursor.execute("SELECT A_Number,Class,Fare,Departure from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s",[s,d,depart])
        NOP = int(NOP)
        request.session['NOP'] = NOP
        request.session['n'] = NOP
        if res_count>0:
            avf = cursor.fetchall()
            connection.close()
            return render(request,'mysite3/details.html',{'avf':avf})
        else:
            connection.close()
            return render(request,'mysite3/details-no-flight.html')
    else:
        data = Airport.objects.all()
        return render(request,'mysite3/index1.html',{'data':data})


def details(request):
    if request.method=='GET':
        return render(request,'mysite3/details.html')
    if request.method=='POST':
        options = request.POST.get('a1')
        avf = options
        request.session['options'] = options
        #options=tuple(options[1:-1].split(','))
        #option1=tuple(filter(None, options.split(',')))
        #option1=eval(options)
        #,{'options':options,'val':val1,'val1':val2}
        
        #return render('mysite3/details',{'avf':avf})
        return render(request,'mysite3/payerdetails.html')
    return render(request,'mysite3/payerdetails.html')
       

    #else:
        #options = request.POST.getlist('options')
        #return render(request,'mysite3/payerdetails.html')

def forms(request):
    if request.method=='GET':
        
        return render(request,'mysite3/forms.html')
    elif request.method=='POST':
        fname = request.POST.get('first_name')
        mname = request.POST.get('middle_name')
        lname = request.POST.get('last_name')
        em = request.POST.get('EMAIL')
        nationality = request.POST.get('nat')
        age = request.POST.get('Age')
        age = int(age)
        ph_no = request.POST.get('Phone_no.')
        ph_no = str(ph_no)
        fname = str(fname)
        mname = str(mname)
        lname = str(lname)
        em = str(em)
        nationality = str(nationality)
        category = request.POST.get('category')
        category = int(category)
        cat=Discounts.objects.get(category=category)
        cursor = connection.cursor()
        #cursor.execute("Select Category from Discounts where Name=%s",[category])
        #c = cursor.fetchall();
        #cat = c[0]
        PID=BookingDetails.objects.get(payerid=PayerID)
        p1 = Passenger(firstname=fname,middlename=mname,lastname=lname,email=em,nationality=nationality,age=age,phone_no=ph_no,payerid=PID,category=cat)
        p1.save()
        cursor.execute("Select ")             
        totalcost
        return render(request,'mysite3/forms.html')
    else:
        return render(request,'mysite3/finalpage.html')

def payerdetails(request):
    if request.method=='GET':
        return render(request,'mysite3/payerdetails.html')
    elif request.method=='POST':
        c = connection.cursor()
        fname = request.POST.get('first_name')
        mname = request.POST.get('middle_name')
        lname = request.POST.get('last_name')
        #em = request.POST.get('EMAIL')
        ph_no = request.POST.get('phone_no.')
        #global FlightID,FareID,Bookingdate,Totalcost
        #option1=tuple(filter(None, options.split(',')))
        options = request.session['options']
        val1=options[-2:-1]
        val2=options[-5:-4]
        FlID=int(val2)
        FlightID=FlightSchedule.objects.get(fs_id=FlID)
        FID=int(val1)
        FareID=Fare.objects.get(fareid=FID)
        Bookingdate=str(datetime.datetime.now().date())
        NOP = request.session['NOP']
        #nationality = request.POST.get('nat')
        #age = request.POST.get('Age')
        #ph_no = request.POST.get('Phone_no.')
        #category = request.POST.get('category')
        fname = str(fname)
        mname = str(mname)
        mname = str(mname)
        lname = str(lname)
        ph_no = str(ph_no)
        b1 = BookingDetails(firstname=fname,middlename=mname,lastname=lname,phone_no=ph_no,bookingdate=Bookingdate,num_of_seats=NOP,fareid=FareID,flight=FlightID)
        b1.save()
        c.execute("SELECT PayerID from booking_details where Phone_no=%s",[ph_no])
        res = c.fetchone()
        global PayerID
        PayerID = res[0]
        #PayerID = Booking_Details.object ,'val1':val1,'val2':val2
        NOP = int(NOP)
        n = request.session['n']
        n = int(n)
        return render(request,'mysite3/forms.html',{'NOP':range(1,NOP+1),'n':n})
    return render(request,'mysite3/forms.html')

def finalpage(request):
    return render(request,'mysite3/finalpage.html')

import MySQLdb

#def list(request):
#    db = MySQLdb.connect(user='root', db='A',  passwd='rizwan1998', host='localhost')
#    cursor = db.cursor()
#    cursor.execute('SELECT * FROM Aircraft')
#    names = [row[0] for row in cursor.fetchall()]
#    db.close()i
#    return render(request, 'list.html', {'names': names})

'''class AirportCreateView(CreateView):
    model = Airport
    fields = ('city')
    success_url = reverse_lazy('person_changelist')'''
