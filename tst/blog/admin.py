from django.contrib import admin

from .models import Topic, Post, Section


class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', 'posts')

class PostAdmin(admin.ModelAdmin):
	list_display = ('number', 'title', 'date', 'topic',)
	list_filter = ('topic',)

class SectionAdmin(admin.ModelAdmin):
	list_display = ('post', 'number', 'heading',)
	list_filter = ('post',)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Section, SectionAdmin)