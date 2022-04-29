from plans.models import Booking
from django.core import mail
from django.utils import timezone
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval', seconds=60)
def toexpire():
    DT = timezone.now()
    bookings = Booking.objects.all()
    for booking in bookings:
        name = booking.firstname
        email = booking.email
        isExpired = booking.isExpired
        expiredDate = booking.expiresDate
        if DT > expiredDate:
            isExpired = True
            mail.send_mail(
                 'Expired',
                 name + ' plan has expired ',
                 'booking@village.ng',
                 ['maduabuchiokonkwo@gmail.com']
            )

scheduler.start()
# scheduler.add_job(toexpire, 'interval', seconds=60)
# print("sending notifications")
# try:
    
# except:
#     print(error)

   
# from apscheduler.schedulers.blocking import BlockingScheduler

# # sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')
# sched.start()




        




