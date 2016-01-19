from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Topic(models.Model):
	name = models.TextField(unique=True)
	name_slug = models.SlugField()

	def __str__(self):
		return self.name


class Subtopic(models.Model):
	topic = models.ForeignKey(Topic, related_name='subtopics')
	name = models.TextField(unique=True)
	name_slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Post(models.Model):
	subtopic = models.ForeignKey(Subtopic, related_name='posts')
	name = models.TextField(unique=True)
	name_url = models.TextField()
	date_pub = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']


class Section(models.Model):
	post = models.ForeignKey(Post, related_name='sections')
	short_desc = models.TextField()
	long_desc = models.TextField(blank=True)
	heading = models.TextField()
	content = models.TextField()
	summary = models.TextField(blank=True)

	def __str__(self):
		return self.post.name

	class Meta:
		ordering = ['pk']