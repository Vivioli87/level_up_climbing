from django.contrib import admin
from .models import GeneralContact, PrivateCoachingContact


class GeneralContactAdmin(admin.ModelAdmin):

    fields = ('full_name', 'email', 'phone_number', 'message')


class PrivateCoachingContactAdmin(admin.ModelAdmin):

    fields = ('full_name', 'email', 'phone_number',
              'message', 'level', 'venue')


admin.site.register(GeneralContact, GeneralContactAdmin)
admin.site.register(PrivateCoachingContact, PrivateCoachingContactAdmin)