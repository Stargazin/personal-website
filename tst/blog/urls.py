from django.conf.urls import url

from .views import BlogPostView, BlogHomeView


urlpatterns = [
	url(r'^post/$', BlogPostView.as_view(), name='blog'),
	url(r'^$', BlogHomeView.as_view(), name='blog_home'),
]