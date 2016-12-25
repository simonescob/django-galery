# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import ViewImage
from .forms import UploadForm
# Create your views here.

@login_required
def index(request, user_id):
	if not request.user.is_authenticated:
		return redirect('login')

	user = get_object_or_404(User, username=user_id)
	if request.user == user:
		data = ViewImage.objects.filter(user=user)
		if request.method == 'POST':
			form = UploadForm(request.POST or None, request.FILES or None, instance=user)
			if form.is_valid():
				imagen = form.cleaned_data['imagen']
				fotos = ViewImage(user=request.user,imagen=imagen)
				fotos.save()
				messages.success(request, "imagen subida exitosamente")
				return redirect(reverse('foto-index', kwargs={'user_id':request.user}))
			else:
				messages.error(request, "No has subido nada")
		else:
			form = UploadForm()
		return render(request, 'fotos/fotos.html', {'fotos':data, 'form':form})
	else:
		messages.error(request, "no eres %s " % request.user)
	return render(request, 'fotos/fotos.html')

@login_required
def upload_image(request):
	if request.method == 'POST':
		form = UploadForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			imagen = form.cleaned_data['imagen']
			fotos = ViewImage(imagen=imagen)
			fotos.save()
			return redirect(reverse('foto-index'))
	else:
		form = UploadForm()
	return render(request, 'fotos/subir.html', {'form':form})

@login_required
def detail_img(request, user_id, img_id):
	user = get_object_or_404(User, username=user_id)
	if request.user == user:
		img = get_object_or_404(ViewImage, id=img_id)
		user = get_object_or_404(User, username=user_id)
		return render(request, 'fotos/img_detail.html', {'img':img})
	else:
		messages.error(request, "no eres %s " % request.user)
	return render(request, 'fotos/fotos.html')

@login_required
def edit_img(request, user_id, img_id):
	user = get_object_or_404(User, username=user_id)
	if request.user == user:
		img = get_object_or_404(ViewImage, pk=img_id)
		form = UploadForm(request.POST or None, request.FILES or None, instance=img)
		if form.is_valid():
			img = form.save()
			img.save()
			messages.success(request, "imagen edita exitosamente")
			return redirect(reverse('foto-index', kwargs={'user_id':request.user}))
		else:
			messages.error(request, "no has actualizado nada")
		return render(request, 'fotos/edit.html', {'form':form, 'img':img})
	else:
		messages.error(request, "no eres %s " % request.user)
	return render(request, 'fotos/fotos.html')

@login_required
def delete_img(request, user_id,img_id):
	user = get_object_or_404(User, username=user_id)
	if request.user == user:
		img = get_object_or_404(ViewImage, pk=img_id)
		form = UploadForm(request.POST or None, request.FILES or None, instance=img or None)
		if form.is_valid():
			img = form.save()
			img.delete()
			messages.success(request, "imagen borrada exitosamente")
			return redirect(reverse('foto-index', kwargs={'user_id':request.user}))
		else:
			messages.error(request, "no has actualizado nada")
		return render(request, 'fotos/delete.html', {'img':img})
	else:
		messages.error(request, "no eres %s " % request.user)
	return render(request, 'fotos/fotos.html')









