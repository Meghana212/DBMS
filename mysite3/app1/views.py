from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.forms import FormIn
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Airport,Passenger,BookingDetails,Fare,FlightSchedule,Discounts
from django.db import connection
from django.template import Context, Template
from django.template.defaulttags import register
FlightID =1
FareID=1
Bookingdate =""
totalcost=0
Ph_no=0
totalcost=0
aid=17
i=1
import datetime
# Create your views here.

def index(request):
    if request.method=='GET':
        data = Airport.objects.all()
        return render(request,'mysite3/index1.html',{'data':data})
    elif request.method=='POST':
        cursor = connection.cursor()
        fro = request.POST.get('from')
        fro = str(fro)
        to = request.POST.get('to')
        to = str(to)
        NOP = request.POST.get('NOP')
        request.session['fro'] = fro
        request.session['to'] = to
        cursor.execute("call GetAP_ID(%s,@sr)",[fro])
        cursor.execute("SELECT @sr")
        s1 = cursor.fetchall()
        s = s1[0]
        #s1 = cursor.fetchall()
        #s = s1[0]
        request.session['source'] = s
        #cursor.execute("SELECT ap_id from airport where city=%s",[to])
        cursor.execute("call GetAP_ID(%s,@de)",[to])
        cursor.execute("SELECT @de")
        d1 = cursor.fetchall()
        d = d1[0]
        #d1 = cursor.fetchone()
        #d = d1[0]
        request.session['dest'] = d
        depart = request.POST.get('depart')
        request.session['depart']=depart
        #arrival = request.POST.get('arrival')
        depart = str(depart)
        depart = depart + '%'
        e = "Economy%"
        b = "Business%"
        f = "First%"
        res_count=cursor.execute("SELECT A_Number,Class,Fare,Departure,Economy_RCapacity 'Available seats',FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and Economy_RCapacity>=%s UNION SELECT A_Number,Class,Fare,Departure,BusinessClass_RCapacity,FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and BusinessClass_RCapacity>=%s UNION SELECT A_Number,Class,Fare,Departure,FirstClass_RCapacity,FS_ID,FareID from aircraft a,fare f,flight_schedule fs,Route r where r.source_airport=%s and r.destination_airport = %s and r.R_ID=f.Route and f.Route = fs.R_ID and a.A_ID=fs.Aircraft and fs.Departure like %s and f.class like %s and FirstClass_RCapacity>=%s",[s,d,depart,e,NOP,s,d,depart,b,NOP,s,d,depart,f,NOP]);
       # NOP = int(NOP)
        request.session['NOP'] = NOP
        request.session['n'] = NOP
        
        #air=""
        if res_count>0:
            avf = cursor.fetchall()
            #air=str(avf)
            #request.session['air'] = air
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
        request.session['options'] = options
        return render(request,'mysite3/payerdetails.html')
    return render(request,'mysite3/payerdetails.html')
       
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
        options = request.session['options']
        classsel = str(options)
        res = classsel.find('Economy')
        if res!=-1:
            class_s = 'Economy'
        else:
            res = classsel.find('Business')
            if res!=-1:
                class_s = 'Business'
            else:
                class_s = 'First'
        val1=options[-2:-1]
        val2=options[-5:-4]
        FlID=int(val2)
        request.session['FS_ID']=FlID
        FlightID=FlightSchedule.objects.get(fs_id=FlID)
        FID=int(val1)
        FareID=Fare.objects.get(fareid=FID)
        Bookingdate=str(datetime.datetime.now().date())
        NOP = request.session['NOP']
        fname = str(fname)
        mname = str(mname)
        mname = str(mname)
        lname = str(lname)
        ph_no = str(ph_no)
        b1 = BookingDetails(firstname=fname,middlename=mname,lastname=lname,phone_no=ph_no,bookingdate=Bookingdate,num_of_seats=NOP,fareid=FareID,flight=FlightID,class_field=class_s)
        b1.save()
        c.execute("SELECT PayerID from booking_details where Phone_no=%s",[ph_no])
        res = c.fetchone()
        PayerID = res[0]
        request.session['payerid'] = PayerID
        n = request.session['n']
        n=int(n)
        n=n+1
        return render(request,'mysite3/forms.html',{'i':i,'n':n})
    return render(request,'mysite3/forms.html')

def forms(request):
    if request.method=='GET':
        return render(request,'mysite3/forms.html')
    elif request.method=='POST':
        n = request.session['n']
        n=int(n)
        m=n+1
        global i
        if i<=n:
            i = i+1
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
            payerid = request.session['payerid']
            Payerid=int(payerid)
            PID=BookingDetails.objects.get(payerid=Payerid)
            p1 = Passenger(firstname=fname,middlename=mname,lastname=lname,email=em,nationality=nationality,age=age,phone_no=ph_no,payerid=PID,category=cat)
            p1.save()
            return render(request,'mysite3/forms.html',{'i':i,'n':m})
        else:
            return render(request,'mysite3/forms.html',{'i':i,'n':m})
    else:
        return render(request,'mysite3/finalpage.html')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def finalpage(request):
    c = connection.cursor()
    payerid = request.session['payerid']
    payerid=str(payerid)
    num = c.execute("Select P_ID,FirstName,MiddleName,LastName from passenger where PayerID=%s",[payerid])
    passengers = c.fetchall()
    pas = list(passengers)
    request.session['pas'] = pas
    #p_ids=[]
    p_id=()
    fares=()
    discounts = ()
    for i in range(0,num):
        p = passengers[i]
        a = str(p)
        p_id=list(p_id)
        p_id.append(int(a[1:3]))
        c.execute("select f.Fare-f.Fare*d.Discount/100 'Fare' from discounts d,booking_details b,passenger p,fare f where p.Category = d.Category and p.PayerID=b.PayerID and f.FareID=b.FareID and P_ID=%s",[p_id[i]])
        fare = c.fetchone()
        a = fare[0]
        fares=list(fares)
        fares.append(float(a))
        c.execute("select d.Discount from discounts d,Passenger p where p.Category = d.Category and P_ID=%s",[p_id[i]])
        d = c.fetchone()
        d = d[0]
        discounts = list(discounts)
        discounts.append(int(d))

    fro = request.session['fro']
    to = request.session['to']
    a_num = request.session['options']
    a_n =str(a_num)
    a_n = a_num[2:9]
    request.session['a_n']=a_n
    dictionary = dict(zip(p_id, fares))
    dictionary_d = dict(zip(p_id, discounts))
    flag = 0
    for i in range(0,len(fares)):
        global totalcost
        totalcost = totalcost + fares[i]
        flag = flag+1
        if flag==len(fares):
            break
    return render(request,'mysite3/finalpage.html',{'passengers':passengers,'p_id':p_id,'fro':fro,'to':to,'a_n':a_n,'totalcost':totalcost,'dictionary':dictionary,'dictionary_d':dictionary_d})

def lastpage(request):
     depart = request.session['depart']
     a_n = request.session['a_n']
     fro = request.session['fro']
     to = request.session['to']
     classsel = request.session['options']
     res = classsel.find('Economy')
     if res!=-1:
         class_s = 'Economy'
     else:
         res = classsel.find('Business')
         if res!=-1:
             class_s = 'Business'
         else:
             class_s = 'First'
     c = connection.cursor()
     s = request.session['source']
     d = request.session['dest']
     depart = str(depart)
     payerid = request.session['payerid']
     payerid=str(payerid)
     c.execute("Select P_ID,FirstName,MiddleName,LastName from passenger where PayerID=%s",[payerid])
     pas = c.fetchall()
     f_id = request.session['FS_ID']
     f_id = str(f_id)
     c.execute("select Departure,Arrival from flight_schedule where fs_id = %s",[f_id])
     time = c.fetchone()
     return render(request,'mysite3/lastpage.html',{'depart':depart,'a_n':a_n,'fro':fro,'to':to,'class_s':class_s,'pas':pas,'time':time})

def admin(request):
    if request.method=='POST':
        uname = request.POST.get('A_id')
        pword = request.POST.get('psw')
        if uname=='admin' and pword=='1234':
            return render(request,'mysite3/edit.html')
        else:
            return render(request,'mysite3/admin.html')
    else:
        return render(request,'mysite3/admin.html')
def editAirport(request):
    if request.method=='GET':
        return render(request,'mysite3/airport.html')
    elif request.method=='POST':
        cty = request.POST.get('city')
        aname = request.POST.get('a_name')
        global aid
        a1 = Airport(ap_id=aid,city=cty,a_name=aname)
        a1.save()
        aid = aid+1
        return render(request,'mysite3/edit.html')
def editAircraft(request):
    if request.method=='GET':
        return render(request,'mysite3/aircraft.html')
    elif request.method=='POST':
        aid = request.POST.get('a_id')
        ac_name = request.POST.get('ac_name')
        Fcapacity = request.POST.get('Fcap')
        Fcapacity = int(Fcapacity)
        Bcapacity = request.POST.get('Bcap')
        Bcapacity = int(Bcapacity)
        Ecapacity = request.POST.get('Ecap')
        Ecapacity = int(Bcapacity)
        a1 = Aircraft(a_id=aid,firstclass_capacity=Fcapacity,businessclass_capacity=Bcapacity,economy_capacity=Ecapacity,a_number=ac_name)
        a1.save()
        return render(request,'mysite3/edit.html')




