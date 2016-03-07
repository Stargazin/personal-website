from __future__ import absolute_import

from django.db.models.loading import get_model
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, TemplateView

from .models import Post


class BlogHomeView(ListView):
	template_name = 'blog/blog_home.html'

	def get_queryset(self):
		model = get_model('blog', 'Post')
		self.posts = get_list_or_404(model.objects.select_related())
		return self.posts

	def get_context_data(self, **kwargs):
		context = super(BlogHomeView, self).get_context_data(**kwargs)
		context['posts'] = self.posts
		return context

class BlogPostView(ListView):
	template_name = 'blog/blog_post.html'

	def get_queryset(self):
		model = get_model('blog', 'Post')
		self.post = get_object_or_404(model.objects.select_related(), title_url=self.kwargs['post'])
		return self.post

	def get_context_data(self, **kwargs):
		if len(self.post.sections.all()) > 1:
			sectioned_post = True
		else:
			sectioned_post = False

		context = super(BlogPostView, self).get_context_data(**kwargs)
		context['post'] = self.post
		context['sectioned_post'] = sectioned_post
		return context

class DevView(TemplateView):
	template_name = 'blog/blog_dev.html'