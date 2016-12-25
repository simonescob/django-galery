from django.shortcuts import render
from .models import Notification

from .forms import NotiForm
# Create your views here.

def index_noti(request):
	n = Notification.objects.filter(user=request.user)
	form = NotiForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		text = form.cleaned_data['text']
		image = form.cleaned_data['image']
		noti = Notification(user=request.user, text=text, image=image)
		noti.save()
	return render(request, 'noti/index.html', {'noti':n, 'form':form})