from django.contrib import admin
from .models import ViewImage

# Register your models here.
# @admin.register(ViewImage)
class FotoAdmin(admin.ModelAdmin):
	list_display = ('user', 'imagen')
	list_filter = ['user']

admin.site.register(ViewImage, FotoAdmin)