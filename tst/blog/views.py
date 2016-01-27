from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.base import TemplateView


class BlogPostView(TemplateView):
	template_name = 'blog/blog_post.html'

class BlogHomeView(TemplateView):
	template_name = 'blog/blog_home.html'