from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	image = models.ImageField(upload_to='noti')