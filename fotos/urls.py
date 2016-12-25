from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="foto-index"),
	url(r'^(?P<img_id>[0-9]+)/$', views.detail_img, name="foto-detail"),
	url(r'^(?P<img_id>[0-9]+)/edit/$', views.edit_img, name="foto-edit"),
	url(r'^(?P<img_id>[0-9]+)/delete/$', views.delete_img, name="foto-delete"),
	url(r'^upload/$', views.upload_image, name="foto-upload"),
]