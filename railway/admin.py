from django.contrib import admin

# Register your models here.
from .models import Register,Add_Train,Add_route,Passenger,Book_ticket,Asehi,ContactUsForm

admin.site.register(Register)
admin.site.register(Add_Train)
admin.site.register(Add_route)
admin.site.register(Passenger)
admin.site.register(Book_ticket)
admin.site.register(Asehi)
admin.site.register(ContactUsForm)