from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User)
	photo = models.ImageField(upload_to='perfiles', null=True, blank=True)

	def __str__(self):
		return self.user.username