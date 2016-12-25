from django import forms
from .models import Notification

class NotiForm(forms.ModelForm):
	class Meta:
		model = Notification
		fields = ['text', 'image']



