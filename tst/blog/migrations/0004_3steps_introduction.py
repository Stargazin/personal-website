# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify


def load_post(apps, schema_editor):
	Topic = apps.get_model('blog', 'Topic')
	Post = apps.get_model('blog', 'Post')
	Section = apps.get_model('blog', 'Section')

	life = Topic.objects.get(name='life')
	topic = life


	post = Post(topic=topic,
		title='What is "3 Steps Taken" You Ask?',
		#title_url='',
		number='2',
		date='February 17th, 2016',
		summary='3 steps taken this. 3 steps taken that. What does 3 steps taken actually mean? Wait. Who am I? I\'m a biologist. Wait. I\'m also a web developer! Find out more about me and this blog!')
	post.save()

	section1 = Section(post=post,
		number='1',
		heading='Why hello there and welcome to my blog',
		content='<p>I\'m Alex, a biologist from UC Santa Barbara turned web developer. Yeah, you\'re right -- there\'s no relation between the two at all. And the only real experience I had was an introductory seminar in my last quarter. So why make the switch?</p>\n\n<p>The biggest draw for me was the thought of having an idea and being able to create it. Take this blog for example. Four months ago, I didn\'t even know how to follow a tutorial to bootstrap a simple blog layout. Now not only can I do that, I can customize to my heart\'s content and even write from scratch if need be! Four months ago, I didn\'t even know how to solve FizzBuzz. Now not only can I do that (with multiple languages!), I can set up a working backend using an MVC framework like Django! That\'s the second biggest reason: I feel like my learning translates to results.</p>\n\n<p>Take a look back at my undergrad with me. In my third year, I took the biochemistry series. No matter how much I learned in one quarter, I was not better off in the next. The "knowledge" I gained had no application from quarter to quarter. To be honest, it would be fair to say that there was often very little application even from midterm to midterm. (There were definitely exceptions with great professors though!) To draw a comparison to programming, everything was as high-level as could be. As a result, there was often an emphasis on memorization and rarely a need for understanding.</p>\n\n<p>Don\'t get me wrong though. I love biology and "biologist from UCSB" is still one of the ways I describe myself. If I had the opportunity to redo it all, I\'d for sure walk the same path (and start learning to program earlier of course).</p>')
	section1.save()

	section2 = Section(post=post,
		number='2',
		heading='3 (steps taken) is the magic number',
		content='<p>"One step forward; two steps back." I\'m sure we\'ve all heard this idiom before. I started adding "3 steps taken" to it and making it my motto a few years back. The idea is that even if we end up further away from our goal, we\'ve gained experience that actually puts us closer towards it. I think this is a pattern we are trained not to follow. We think this is fundamentally wrong. If we end up further away from our goal than when we started, we must have regressed. I don\'t believe that\'s true at all.</p>\n\n<p>Imagine you\'re at an interview and are asked the following question, "Do you tend to waste your time?" What would you respond to that? Obviously, you would say no. But let\'s think back. If we ever end up futher away from our goal than when we started and that\'s all we take away from it, then by definition, we have wasted our time. But did we really? At the very least, we know not to make the same mistake again. Hopefully we also learned why we made the mistake. Maybe we\'ve thought of an alternative solution or can start working towards one. It\'s more than likely that we in fact did not waste our time.</p>')
	section2.save()

	section3 = Section(post=post,
		number='3',
		heading='My 3 steps taken',
		content='<p>We can learn from just about every experience. Would I be better off now if I had done a computer science degree? In terms of programming? Sure. But not necessarily as an individual. I used to be very scared of anything and everything outside of my comfort zone. It\'s the people who encouraged me to take on harder projects and supported me along the way that allowed me to become someone who approaches everything with confidence and has a firm belief that success is only a matter of time.</p>\n\n<p>I would definitely say that my undergraduate career was a success. I know I could get into any school if I wanted to pursue a higher degree. Sadly, my success as a biologist doesn\'t directly translate in a different field, especially an unrelated one like programming. So what\'s my takeaway? How has my degree in biology helped me become a programmer?</p>\n\n<p>I\'m a much better learner now. I know how I learn, and what I need to do to learn efficiently. I know the importance of fundamentals. I know how to ask effective questions that get me the answers I need.</p>\n\n<p>I\'m a confident person now. It\'s impossible to do my best unless I believe in myself. I\'m going to go through life with people telling me that I can\'t. Shouldn\'t I at the very least tell myself that I can?</p>\n\n<p>I love working with people now. With other people, I can share both the success and the hardship. I have people to encourage me and grow with, and so do they.</p>\n\n<p>The point is, there\'s always a takeaway, but it\'s up to us to take it.</p>')
	section3.save()

	section4 = Section(post=post,
		number='4',
		heading='What else you got?',
		content='<p>It\'s just about impossible to stay motivated all the time. There are going to be days when we don\'t feel like doing anything and times when we feel like we want to quit. I think that\'s pretty normal. At the end of the day, it\'s our desire to progress and grow that keeps us on the hustle. That being said, motivation is nice, so here are some other mottos that I\'ll be keeping in mind as I climb to the top.</p>\n\n<p>"Life is what you make it, but it\'s up to you to take what you deserve. So let\'s go for broke."<br> -- <a href="https://twitter.com/davidsocomedy" class="text-link" target="_blank">David So</a><br><br>Put everything on the line to create the best chances for yourself. Opportunities will knock, so don\'t forget to answer.</p>\n\n<p>"Dominate humbly."<br> -- <a href="https://twitter.com/barbellbrigade" class="text-link" target="_blank">Barbell Brigade</a><br><br>Being better than someone does not mean you are above them. Always look to grow and help others do the same.</p>\n\n<p>"Live for today, look forward to tomorrow, and don\'t forget to smile."<br> -- Some fisherman from an old Cartoon Network show<br><br>Everyone has goals they are working towards. Keep hustling, but don\'t forget to enjoy the ride.</p>')
	section4.save()

	section5 = Section(post=post,
		number='5',
		heading='How about this blog? What\'s it all about?',
		content='<p>This is first and foremost going to be a web development blog. I love to learn and one of the best ways for me to make sure I understand something is to be able to explain it. I want all developers to be able to benefit from my posts, especially those who are relatively new. I couldn\'t have made it this far without the amazing open source community, and I want to play a part in making it even better.</p>\n\n<p>I\'ll also be posting my musings and about my career as a way for me to keep track of how far I\'ve come, and hopefully teach others about the things I\'ve learned along the way. In addition, music is huge part of my life and it\'s always great to remember songs that I consider a part of my soundtrack (bonus: "Be the main character of your life and not the side character of someone else\'s."). These are songs that keep me hustling and hopefully can do the same for you.</p>\n\n<p class="btw">It\'s a lot of electronic music. I won\'t be offended if that\'s not your thing!</p>\n\n<p>Thanks for reading and stay tuned for more to come!</p>')
	section5.save()

	if not post.title_url:
		post.title_url = slugify(post.title)
		post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_vagrant_setup'),
    ]

    operations = [
    	migrations.RunPython(load_post),
    ]