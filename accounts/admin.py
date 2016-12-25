from django.contrib import admin
from .models import UserProfile
# Register your models here.

class AdminUser(admin.ModelAdmin):
	list_display = ('user', 'photo')
	list_filter = ['user']

admin.site.register(UserProfile, AdminUser)