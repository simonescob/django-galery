# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username = forms.CharField(label='nombre de usuario')
	first_name = forms.CharField(label='nombre')
	last_name = forms.CharField(label='apellido')
	email = forms.EmailField(label='correo',widget=forms.EmailInput)
	password = forms.CharField(label='contraseña' ,widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar contraseña' ,widget=forms.PasswordInput)
	photo = forms.ImageField(label='foto de perfil' , required=False, 
		widget=forms.FileInput(attrs={'class':'inputfile'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username):
			raise forms.ValidationError('Ya existe este nombre de usuario, intenta con otro.')
		return username

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2 or password2 != password:
			raise forms.ValidationError('las contraseñas no coinciden')
		return password2

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un email con ese nombre')
		return email

class ImageForm(forms.ModelForm):
	class Meta: 
		model = UserProfile
		fields = ['photo']
		widgets = { 'photo': forms.FileInput(attrs={'class':'inputfile'}) }
		labels = {'photo':'Subir foto'}

class RegisterEdit(forms.ModelForm):
	class Meta:
		model = User
		fields = [
		'username', 
		'last_name', 
		'first_name',
		'email',
		]
		labels = {'username':'Usuario','email':'correo', 'last_name':'Apellido'}
		widgets = {'password':forms.PasswordInput(render_value=False), 'email':forms.EmailInput()}





			

