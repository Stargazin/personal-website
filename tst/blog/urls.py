from django.conf.urls import url
from . import views

urlpatterns = [
	#general
	url(r'^$', views.index, name='index'),
]