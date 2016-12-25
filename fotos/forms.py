from django import forms

from .models import ViewImage

class UploadForm(forms.ModelForm):
	class Meta:
		model = ViewImage
		fields = ['imagen']
		# widgets = { 'imagen': forms.FileInput(attrs={'class':'inputfile'}) }



