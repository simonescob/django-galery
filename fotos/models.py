from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ViewImage(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to="fotos", editable=True)

	def __str__(self):
		return "%s - %s" % ( self.user, self.imagen)