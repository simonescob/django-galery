# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import LoginForm, RegisterForm, ImageForm, RegisterEdit
# Create your views here.

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request,'has ingresado')
				return redirect('/fotos/%s/' % request.user)
			# else:
			# 	messages.error(request,'no has ingresado')
		else:
			messages.error(request,'La contraseña esta mal')
	else:
		form = LoginForm()
	return render(request, 'accounts/login.html', {'form':form})

@login_required()
def logout_view(request):
	logout(request)
	messages.success(request, 'te has salido de sesion')
	return redirect('login')

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			photo = form.cleaned_data['photo']
			# return HttpResponse('%s %s %s' % (username, password,email))

			form_register = User.objects.create_user(username=username, email=email, password=password2, 
				last_name=last_name, first_name=first_name)

			user = UserProfile()
			user.user = form_register
			user.phto = photo
			user.save()
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form':form})

@login_required()
def index(request):
	p = UserProfile.objects.filter(user=request.user).order_by('-user')[:1]
	img = get_object_or_404(UserProfile, pk=p)

	form = ImageForm(request.POST or None, request.FILES or None, instance=img)
	if form.is_valid():
		photo = form.cleaned_data['photo']
		p = UserProfile(user=request.user ,photo=photo)
		p.save()
		return redirect('user-home')

	return render(request, 'accounts/home.html', {'profile':p, 'form':form})

@login_required()
def edit_view(request):
	user = UserProfile.objects.filter(user=request.user)
	form = RegisterEdit(request.POST or None, instance=request.user)
	if form.is_valid():
		formu = form.save(commit=False)
		formu.save()
		return redirect('user-home')
	return render(request, 'accounts/editar.html', {'form':form})