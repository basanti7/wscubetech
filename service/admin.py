from django.contrib import admin
from service.models import Service
from service.models import SubService

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon', 'service_title', 'service_des')

class SubServiceAdmin(admin.ModelAdmin):
    list_display=('sub_service_name',)

admin.site.register(Service,ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
