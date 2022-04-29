from django.db import models
from cloudinary.models import CloudinaryField
from phone_field import PhoneField
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.signals import request_started
from django.dispatch import receiver
now = timezone.now()



# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=100)
    plan_img = CloudinaryField('plan_img', blank=True)
    # plan_img = models.ImageField(upload_to='images/', blank=True)
    price = models.IntegerField(default=0)
    per = models.CharField(max_length=50,blank=True )
    benefit1 = models.CharField(max_length=150, blank=True)
    benefit2 = models.CharField(max_length=150, blank=True)
    benefit3 = models.CharField(max_length=150, blank=True) 
    benefit4 = models.CharField(max_length=150, blank=True)
    benefit5 = models.CharField(max_length=150, blank=True)
    benefit6 = models.CharField(max_length=150, blank=True)
    benefit7 = models.CharField(max_length=150, blank=True)
    benefit8 = models.CharField(max_length=150, blank=True)
    benefit9 = models.CharField(max_length=150, blank=True)
    benefit10 = models.CharField(max_length=150, blank=True)
    benefit11 = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.title

    


class Booking(models.Model):
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    price = models.IntegerField(default=0)
    phone_regex = RegexValidator(regex=r'^[0]\d{10}$',message="must be a valid phone number")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    plan = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True)
    dateBooked= models.DateTimeField(blank=True, null=True, auto_now_add=True)
    expiresDate = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    paid = models.BooleanField(default=False)
    isExpired = models.BooleanField(default=False)
    renewed = models.BooleanField(default=False)



    def __str__(self):
        return self.firstname + " " + self.lastname

@receiver(request_started, sender=Booking)
def set_expriration():
    if timezone.now() >= self.expiresDate:
        self.isExpired = True

    else:
        self.isExpired = False

    
    

        
    # def send_mail(self, email, dateBooked, expiresDate, first_name, last_name):
    #     booked_plan = self.plan.title
    #     email = self.email
    #     admin = 'maduabuchiokonkwo@village.ng'
    #     client = self.first_name + " " + self.last_name
    #     client_phone = self.phone


    #     if datetime.now() - self.dateBooked == 7:
    #         message1 = (
    #             'space about to expire',
    #             'your plan ' + booked_plan + 'will expire in 7 days time',
    #             'maduabuchiokonkwo@gmail.com',
    #             [email]
    #         )
    #         message2=(
    #             'expiration email',
    #             'the user ' + client + 'plan will expire in a week time please call them on' + client_phone + 'they signed up for ' + booked_plan ,
    #             'maduabuchiokonkwo@gmail.com',
    #             ['maduabuchiokonkwo@gmail.com']
    #         )

    #         mail.send_mass_mail((message1, message2), fail_silently=False)

    #     if datetime.now() == self.expiresDate:
        
    #         message1 = (
    #             'plan just expired',
    #             'your plan for ' + booked_plan + ' please call in to book a new plan'
    #             'blogging@village.ng',
    #             [email]
    #         )
    #         message2=(
    #             'expiration email',
    #             'the user ' + client + 'plan just expired for the plan' + booked_plan + 'please restrict their access to the space'
    #             'info@village.ng',
    #             ['maduabuchiokonkwo@gmail.com']
    #         )
    #         mail.send_mass_mail((message1, message2), fail_silently=False)







    


# class Space(models.Model):
#     title = models.CharField(max_length=150)
#     people = models.IntegerField(default=0)
#     floor = models.IntegerField(default=0)
#     space_image = CloudinaryField('space_image', blank=True)
#     isavailable = models.BooleanField(default=True)
#     isPaidfor = models.BooleanField(default=False)
    
    

#     def deactivate_space(self):
#         if self.isPaidfor == True:
#             self.isavailable == True
#         if  self.isavailable == True and datetime.now() > self.dateBooked:
#             self.isavailable = False
            

    

#     def __str__(self):
#         return self.title



# class Booking(models.Model):
#      PLAN_CHOICES = (
#         ('daily', 'daily'),
#         ('regular', 'regular'),
#         ('vip', 'vip'),
#         ('dedicated standard', 'dedicated standard'),
#         ('dedicted classic', 'dedicated classic' ),
#         ('dedicated premium 1', 'dedicated premium 1'),
#         ('dedicated premium 2', 'dedicated premium 2'),
#         ('dedicated premium 3', 'dedicated premium 3'),
#         ('dedicated premium 4', 'dedicated premium 4'),
#         ('dedicated enterprise', 'dedicated enterprise'),
#         ('dedicated single', 'dedicated single'),
#         ('virtual premium', 'virtual premium'),
#         ('virtual lite', 'virtual lite'),
#         ('meeting room 1', 'meeting room 1'),
#         ('meeting room 2', 'meeting room 2'),
#         ('training room', 'training room'),

#     )
#     GROUND_FLOOR_CHOICES = (
#         ('dedicted room for 4', 'Dedicated room for 4'),
#         ('dedicated office for 5', 'Dedicated office for 5'),
#         ('meeting room', 'Meeting room'),
#         ('dedicated office for 10', 'Dedicated office for 10'),
#         ('dedicated office for 6', 'Dedicated office for 6'),
#         ('reception space', 'Reception space'),
        
#     )
#     MIDDLE_FLOOR_CHOICES = (
#         ('training room Soweto', 'Training room Soweto'),
#         ('training room Ago', 'Training room Ago'),
#         ('cafe for hangout or event ', 'Cafe for hangout or event'),
    
#     )
#     TOP_FLOOR_CHOICES = (
#         ('meeting/conference room', 'Meeting/Conference room'),
#         ('dedicated office 1 for 4', 'Dedicated office 1 for 4 '),
#         ('dedicated office 2 for 4', 'Dedicated office 2 for 4'),
#         ('dedicated office 3 for 4', 'Dedicated office 3 for 4'),
#         ('dedicated office 4 for 4', 'Dedicated office 4 for 4'),
#         ('dedicaeted office 5 for 4', 'Dedicated office 5 for 4'),
#         ('enclave', 'Enclave'),
#         ('dedicated office for 3', 'Dedicated office for 3'),
#         ('dedicated office for 10', 'Dedicated office for 10'),
#         ('vip', 'Vip'),
#         ('open space for 19', 'Open space for 19'),
#         ('kitchen', 'Kitchen'),
#         ('reception space', 'Reception space')
#     )
#     villager= models.CharField(max_length=150, blank=True, null=True)
#     email = models.EmailField(max_length=300, blank=True, null=True)
#     phone = PhoneField(blank=True, help_text='Contact phone number')
   
#     groundFloor = models.CharField(max_lenght=100, blank=True, choices=GROUND_FLOOR_CHOICES)
#     middleFloor = models.CharField(max_length=100, blank=True, choices=MIDDLE_FLOOR_CHOICES)
#     topFloor = models.CharField(max_length=100, blank=True, choices=TOP_FLOOR_CHOICES)
#     plan = models.CharField(max_length=50, blank=True, null=True, choices=PLAN_CHOICES)
#     duration = models.IntegerField(blank=True, null=True)
#     dateBooked = models.DateTimeField(auto_now_add=True)
#     expiresDate = models.DateTimeField(blank=True, null=True, auto_now_add=False)
#     isavailable = models.BooleanField(default=True)
#     quantity = models.IntegerField(default=1)


#     def __str__(self):
#         return self.villager
    
#     def get_plan_price(self, quantity, plan):
#         if self.plan == 'daily':
#             return self.quantity * 3000
#         if self.plan == 'regular':
#             return self.quantity * 25000
#         if self.plan == 'vip':
#             return self.quantity * 35000
#         if self.paln == 'dedicated standard':
#             return self.quantity * 60000
#         if self.plan == 'dedicated classic':
#             return self.quantity * 80000
#         if self.plan == 'dedicated premimum 1':
#             return self.quantity * 120000
#         if self.plan == 'dedicated premium 2':
#             return self.quantity * 160000
#         if self.plan == 'dedicated premium 3':
#             return self.quantity * 200000
#         if self.plan == 'dedicated premium 4':
#             return self.quantity * 240000
#         if self.plan == 'entreprise':
#             return self.quantity * 400000
#         if self.plan == 'dedicated single':
#             return self.quantity * 40000
#         if self.plan == 'virtual premium':
#             return self.quantity *100000
#         if self.plan == 'virtual lite':
#             return self.quantity * 10000 
#         if self.plan == 'meeting room 1':
#             return self.quantity * 5000 
#         if self.plan == 'meeting room 2':
#             return self.quantity * 5000 
#         if self.plan == 'training room':
#             return self.quantity * 10000
        

#     def get_expires_date(self):
#         if self.available:
#             self.expiresDate = self.space.Space.expiresDate
#             return self.expiresDate

#     def check_availabilty(self):
#         if self.expiresDate > self.dateBooked:
#             self.isavailable = True
#         else:
#             self.isavailable = False
    
#     def book_space(self, space):
#         if self.space.Space.isavailable == False:
#             return "Sorry you cannot book this space"
#         else:
#             booking = self.model(
#                 villger_name = self.villager,
#                 email = self.email,
#                 phone = self.phone,
#                 space = self.space,
#                 plan = self.plan,
#                 dateBooked = self.dateBooked,
#                 expiers = self.expiresDate,
#                 quantity = self.quantity,
#                 price = get_plan_price(quantity, plan)

#             )

#             booking.save(using=self_.db)
#             return booking

    

#     def send_mail(self, email, dateBooked, expiresDate):
#         if self.expiresDate - self.dateBooked == 7:
#             message1 = (
#                 'space about to expire',
#                 'your booked space' + self.space.title + 'will expire in a week time',
#                 'fromblogging@village.ng',
#                 ['toself.eamil']
#             )
#             message2=(
#                 'expiration email',
#                 'the user self.villager space is about to expire please give him a call',
#                 'fromblogging@village.ng',
#                 ['toadmin@thevillage.ng']
#             )

#             mail.send_mass_mail((message1, message2), fail_silently=False)


    










