from django.contrib import admin
from .models import Notification
# Register your models here.

class AdminNoti(admin.ModelAdmin):
	list_display = ['user', 'image']
	list_filter = ['user']

admin.site.register(Notification, AdminNoti)



