from django.contrib import admin
from .models import Plan, Booking
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'plan', 'price', 'dateBooked', 'expiresDate', 'paid', 'isExpired')
#     search_fields = ('firstname', 'lastname', 'phone', 'isExpired')
    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
#     fieldsets = ()


admin.site.register(Booking, BookingAdmin)
admin.site.register(Plan)

