# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aircraft(models.Model):
    a_id = models.IntegerField(db_column='A_ID', primary_key=True)  # Field name made lowercase.
    firstclass_capacity = models.IntegerField(db_column='FirstClass_Capacity', blank=True, null=True)  # Field name made lowercase.
    businessclass_capacity = models.IntegerField(db_column='BusinessClass_Capacity', blank=True, null=True)  # Field name made lowercase.
    economy_capacity = models.IntegerField(db_column='Economy_Capacity', blank=True, null=True)  # Field name made lowercase.
    a_number = models.CharField(db_column='A_Number', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aircraft'


class Airlinemiles(models.Model):
    p = models.ForeignKey('Passenger', models.DO_NOTHING, db_column='P_ID', primary_key=True)  # Field name made lowercase.
    miles = models.IntegerField(db_column='Miles', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airlinemiles'


class Airport(models.Model):
    ap_id = models.IntegerField(db_column='AP_ID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    a_name = models.CharField(db_column='A_name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'airport'


class App1Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('App1Question', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_choice'


class App1Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app1_question'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookingDetails(models.Model):
    payerid = models.IntegerField(db_column='PayerID', primary_key=True)  # Field name made lowercase.
    passenger = models.ForeignKey('Passenger', models.DO_NOTHING, db_column='Passenger_ID')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    flight = models.ForeignKey('FlightSchedule', models.DO_NOTHING, db_column='Flight', blank=True, null=True)  # Field name made lowercase.
    bookingdate = models.DateField(db_column='BookingDate', blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=15, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('Discounts', models.DO_NOTHING, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    fareid = models.ForeignKey('Fare', models.DO_NOTHING, db_column='FareID', blank=True, null=True)  # Field name made lowercase.
    num_of_seats = models.IntegerField(db_column='Num_of_Seats', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TotalCost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_details'
        unique_together = (('payerid', 'passenger'),)


class Discounts(models.Model):
    category = models.IntegerField(db_column='Category', primary_key=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discounts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fare(models.Model):
    fareid = models.IntegerField(db_column='FareID', primary_key=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    route = models.ForeignKey('Route', models.DO_NOTHING, db_column='Route', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fare = models.IntegerField(db_column='Fare', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fare'


class FlightSchedule(models.Model):
    fs_id = models.IntegerField(db_column='FS_ID', primary_key=True)  # Field name made lowercase.
    departure = models.DateTimeField(db_column='Departure', blank=True, null=True)  # Field name made lowercase.
    arrival = models.DateTimeField(db_column='Arrival', blank=True, null=True)  # Field name made lowercase.
    aircraft = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='Aircraft', blank=True, null=True)  # Field name made lowercase.
    r = models.ForeignKey('Route', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flight_schedule'


class Passenger(models.Model):
    p_id = models.IntegerField(db_column='P_ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passenger'


class Route(models.Model):
    r_id = models.IntegerField(db_column='R_ID', primary_key=True)  # Field name made lowercase.
    source_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='Source_Airport', blank=True, null=True, related_name='src')  # Field name made lowercase.
    destination_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='Destination_Airport', blank=True, null=True,related_name='dest')  # Field name made lowercase.
    intermediate_stops = models.IntegerField(db_column='Intermediate_Stops', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'route'
