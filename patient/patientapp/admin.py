from django.contrib import admin
from .models import booking1, department1, doctors1

# Register your models here.

admin.site.register(department1)
admin.site.register(doctors1)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email',
    'doc_name','booking_date','booked_on')
admin.site.register(booking1,BookingAdmin)