from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.BlogHomeView.as_view(), name='blog_home'),
	url(r'^dev/$', views.DevView.as_view(), name='dev_view'),
	url(r'^(?P<post>[\w\-]+)/$', views.BlogPostView.as_view(), name='blog_post'),
]