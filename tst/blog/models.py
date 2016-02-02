from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Topic(models.Model):
	name = models.TextField(unique=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	topic = models.ForeignKey(Topic, related_name='posts')
	title = models.TextField(unique=True)
	title_url = models.TextField(blank=True)
	number = models.TextField(unique=True)
	date = models.TextField(blank=True)
	summary = models.TextField(blank=True)
	review = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['number']

class Section(models.Model):
	post = models.ForeignKey(Post, related_name='sections')
	number = models.TextField(blank=False)
	heading = models.TextField(blank=False)
	content = models.TextField(blank=False)

	def __str__(self):
		return self.heading

	class Meta:
		ordering = ['number']