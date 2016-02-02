from django.conf.urls import url

from .views import BlogPostView, BlogHomeView


urlpatterns = [
	url(r'^$', BlogHomeView.as_view(), name='blog_home'),
	url(r'^(?P<post>[\w\-]+)/$', BlogPostView.as_view(), name='blog_post'),
]