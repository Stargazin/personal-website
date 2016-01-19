from django.conf.urls import url

from .views import BlogPostView


urlpatterns = [
	url(r'^$', BlogPostView.as_view(), name='blog'),
	# url(r'^post/$,')
]