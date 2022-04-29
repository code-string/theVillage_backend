from django.shortcuts import render,get_object_or_404, redirect
from .models import Plan, Booking
from .forms import BookingForm
from django.core import mail
from django.utils import timezone
import schedule
import time
from background_task import background
from apscheduler.schedulers.blocking import BlockingScheduler


# Create your views here.

def plan_list(request):
    plan = Plan.objects.all()
    context = {
        'plans': plan
    }

    return render(request, 'plan/plans.html', context)


def plan_detail(request, plan_id, plan_title, plan_price):
    plans = get_object_or_404(Plan, id=plan_id)
    price = plans.price
    if request.method == 'POST':
        form = BookingForm(plan_title, plan_price, request.POST or None)
        if form.is_valid():
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            phone = request.POST['phone']
            price = plans.price
            plan = plans.title
            price_str = str(plans.price)
            plan_str = str(plans.title)
            form.save()

            message1 = (
                'Congratulations',
                'thank you for booking  a place with us  your plan is ' + plan_str + ' your price is  '  + price_str + ' please call in to make your payment',
                'booking@village.ng',
            [email]
            )
            message2=(
                'a new signup',
                'a new client ' + first_name + " " + last_name + " just signed up please call then on " + phone,
                'booking@village.ng',
                ['maduabuchiokonkwo@gmail.com']
            )

            mail.send_mass_mail((message1, message2), fail_silently=False)
            return redirect('index')
    else:
        form = BookingForm(plan_title, plan_price)
    
    context = {
        'plan': plans,
        'form': form
    }

    return render(request, 'plan/plan_detail.html', context)



# def expired_plan():
#     bookings = Booking.objects.filter(isExpired=True)
#     # emails = bookings.email.all()
#     # admins = ['dapo@village.ng', 'james@village.ng', 'sam@village.ng']
#     admins = 'maduabuchiokonkwo@gmail.com'
#     support = 'booking@village.ng'

   
#     for booking in bookings:
#         name = booking.firstname
#         email = booking.email
#         phone = booking.phone
#         message1 = (
#             'Booking Expired',
#             'Dear ' + name + ' your plan with us at thevillage just expired. You can reach us immediately at 07089996339 for to renew',
#             support,
#             [email]
#         )

#         message2 = (
#             'Expired plan',
#             'Please call ' + name + ' at ' + phone + ' their plan has expired',
#             support,
#             ['maduabuchiokonkwo@gmail.com']
#         )
#         mail.send_mass_mail((message1, message2), fail_silently=False)


# @background(schedule=2)
# def notify_user():
#     bookings = Booking.objects.all()
#     support = 'booking@village.ng'
#     if bookings.isExpired == True:
#         for booking in bookings:
#             email = booking.email
#             phone = booking.phone
#             for booking in bookings:
#                 name = booking.firstname
#                 email = booking.email
#                 phone = booking.phone
#                 message1 = (
#                     'Booking Expired',
#                     'Dear ' + name + ' your plan with us at thevillage just expired. You can reach us immediately at 07089996339 for to renew',
#                     support,
#                     [email]
#                 )

#                 message2 = (
#                     'Expired plan',
#                     'Please call ' + name + ' at ' + phone + ' their plan has expired',
#                     support,
#                     ['maduabuchiokonkwo@gmail.com']
#                 )
#                 mail.send_mass_mail((message1, message2), fail_silently=False)

#     elif booking.expiresDate - timezone.now == 7:
#         for booking in bookings:
#             email = booking.email
#             phone = booking.phone
#             for booking in bookings:
#                 name = booking.firstname
#                 email = booking.email
#                 phone = booking.phone
#                 message1 = (
#                     'Booking Expired',
#                     'Dear ' + name + ' your plan with us at thevillage just expired. You can reach us immediately at 07089996339 for to renew',
#                     support,
#                     [email]
#                 )

#                 message2 = (
#                     'Expired plan',
#                     'Please call ' + name + ' at ' + phone + ' their plan has expired',
#                     support,
#                     ['maduabuchiokonkwo@gmail.com']
#                 )
#                 mail.send_mass_mail((message1, message2), fail_silently=False)
#     else:

#         message2 = (
#             'Expired plan',
#             'Please call ' + name + ' at ' + phone + ' their plan has expired',
#             support,
#             ['maduabuchiokonkwo@gmail.com']
#         )
#         mail.send_mail(message2, fail_silently=False)
        
        
    


# schedule.every(10).seconds.do(expired_plan)
# schedule.run_pending()


# def to_be_expired():
#      admins = 'maduabuchiokonkwo@gmail.com'
#      support = 'booking@village.ng'
#      bookings = Booking.objects.all()
#      for booking in bookings:
#         name = booking.firstname + " " + booking.lastname
#         email = booking.email
#         phone = booking.phone
#         message1 = (
#             'Booking to expire in a week ',
#             'Dear ' + name + ' your plan with us will expire in a week time ', 
#             support,
#             [email]
#         )
#         message2 = (
#             'Booking to expire in a week',
#             'Please call ' + name  + ' at ' +  phone + ' their plan will expire in a week time ',
#             support,
#             ['maduabuchiokonkwo@gmail.com']
#         )
#         mail.send_mass_mail((message1, message2), fail_silently=False)
        
   




    # to_be_expired()



# def toexpire():
#     DT = timezone.now()
#     bookings = Booking.objects.all()
#     for booking in bookings:
#         name = booking.firstname
#         email = booking.email
#         isExpired = booking.isExpired
#         expiredDate = booking.expiresDate
#         if DT > expiredDate:
#             isExpired = True
#             mail.send_mail(
#                  'Expired',
#                  name + ' plan has expired ',
#                  'booking@village.ng',
#                  ['maduabuchiokonkwo@gmail.com']
#             )



# scheduler = BlockingScheduler()
# scheduler.add_job(toexpire, 'interval', seconds=60)
# print("sending notifications")
# try:
#     scheduler.start()
# except:
#     print(error)








