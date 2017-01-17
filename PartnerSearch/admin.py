from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Institution)
admin.site.register(Programme)
admin.site.register(UserAttribute)

admin.site.register(UserInterestTo)


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('institution_name','country',)


class SubmitRequestAdmin(admin.ModelAdmin):
    list_display = ('sr_user','sr_institution','type_of_Submit')


admin.site.register(Institution,InstitutionAdmin)
admin.site.register(SubmitRequest,SubmitRequestAdmin)