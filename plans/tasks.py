import celery
from django.utils import timezone
from plans.models import Booking
from django.core import mail   
from celery.task.schedules import crontab
from celery.decorators import periodic_task
import time



def send_message(topic, body, support_mail, user_email):
    return mail.send_mail(
        topic,
        body,
        support_mail,
        [user_email]
    )


@periodic_task(run_every=(crontab(minute='*/1')), name="check-expiration", ignore_result=True)
def notify_user():
    bookings = Booking.objects.filter(renewed=False)
    send_message("plan expired ", "no activity today",  "booking@village.ng", "maduabuchiokonkwo@gmail.com")
    # DT = timezone.now().date()
    # for booking in bookings:
    #     email = booking.email
    #     expiresTime = booking.expiresDate
    #     expiresTime = expiresTime.date()
    #     name = booking.firstname
    #     plan = booking.plan
    #     phone = booking.phone
    #     isExpired = booking.isExpired
    #     if (expiresTime - DT).days  == 7:
    #         send_message("plan to  expire soon", " your " + " " + plan + " " + " plan with us  will expire in 7 days ", "booking@village.ng", email )
    #         send_message("plan to expire ", "please call " + name + " at " + phone + " their plan, " + plan + " will expire in 7 days", "booking@village.ng", "maduabuchiokonkwo@gmail.com")
    #     elif (DT - expiresTime).days == 0:
    #         isExpired = True
    #         send_message("plan expired", "Hi " + name + " your " + plan + " plan  with us has expired please call 08063572194  for renewal", "booking@village.ng", email)
    #         send_message("plan expired ", "Hi  please  call " + name + " their plan just expired phone number is " + phone + " and remember to turn their plan to expired", "booking@village.ng", "maduabuchiokonkwo@gmail.com")
    #     elif (DT - expiresTime).days == 3:
    #         send_message("plan expired", "Hi " + name + " your " + plan + " plan  will expire in 3 days  please call 08063572194  for renewal", "booking@village.ng", email)
    #         send_message("plan expired ", "Hi  please  call " + name + " their plan will expire in 3 days pleas call them with  " + phone,  "booking@village.ng", "maduabuchiokonkwo@gmail.com")
    #     else:
    #        send_message("plan expired ", "no activity today",  "booking@village.ng", "maduabuchiokonkwo@gmail.com")
        
    

