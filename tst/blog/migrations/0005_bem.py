# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify


def load_post(apps, schema_editor):
	Topic = apps.get_model('blog', 'Topic')
	Post = apps.get_model('blog', 'Post')
	Section = apps.get_model('blog', 'Section')

	web = Topic.objects.get(name='web')
	topic = web

	post = Post(topic=topic,
		title='Class Naming With BEM Methodology',
		#title_url='',
		number='3',
		date='March 1st, 2016',
		summary='Reading code is hard. Reading unorganized code is even harder. HTML and CSS can get jumbled up into a mess because of elements with random names and selector nesting in CSS. This can lead to large technical debts due to specificity issues, unintentional overrides, and overall unmaintainable code. In this post, we\'ll take a look at how to keep our HTML and CSS consistent and organized using the BEM methodology.')
	post.save()

	section = Section(post=post,
		number='1',
		heading='Starting with an example',
		content='<p>We\'ll start by looking at an example containing a header and footer. The header will have some navigation links, a greeting message, and a call-to-action (cta) button. The footer will have two navigation links also found in the header.</p>\n\n<pre><code class="language-markup">\n&lt;header>\n\n  &lt;div class="nav">\n    &lt;a class="home">&lt;Home/a>\n    &lt;a>&lt;About/a>\n    &lt;a>&lt;Blog/a>\n  &lt;/div>\n\n  &lt;div class="greeting">\n    &lt;p class="text">Hey you!&lt;/p>\n  &lt;/div>\n  \n  &lt;button class="cta">\n    &lt;p class="text">Click here!&lt;/p>\n  &lt;/button>\n\n&lt;/header>\n\n&lt;footer>\n  &lt;a class="home">Back Home&lt;/a>\n  &lt;a class="about">More About Us&lt;/a>\n&lt;/footer>\n</code></pre>\n\n<p>This is easy to understand and work with, but there are things that may lead to headaches in larger projects. Here are a two points as an example:</p>\n\n<p>We have a <code class="inline">&lt;p></code> element inside both <code class="inline">.greeting</code> and <code class="inline">.cta</code> with the same class name (<code class="inline">.text</code>). If we want to style the two <code class="inline">.text</code> elements differently, we would have to nest our selectors.</p>\n\n<pre><code class="language-scss">\n.text {} //Styles both elements.\n\n/* Styles specific element. */\n.greeting .text { color: white; }\n\n.cta .text { color: black; }\n</code></pre>\n\n<p>Similarly, we can\'t just style the "Back Home" link in our <code class="inline">&lt;footer></code> using <code class="inline">.home</code> because it would affect the "Home" link in our header, and vice versa.</p>\n\n<pre><code class="language-scss">\n.home {} //Styles both elements.\n\n/* Styles specific element. */\n.nav .home {}\n\nfooter .home {}\n</code></pre>\n\n<p class="btw">The trend is that we are making our CSS more complex in order to make our styles work correctly. The more we nest selectors, the more likely we are to find <a href="https://css-tricks.com/specifics-on-css-specificity/" class="text-link" target="_blank">specificity</a> issues.</p>\n\n<p>At this point, you might be thinking that you would never write your HTML and CSS like this, so you would never actually run into the problems in this example. That may true, but as projects get bigger, coming up with consistent, unique, and descriptive class names becomes harder. You may end up naming one class <code class="inline">.home-link-header</code> early on and name another class <code class="inline">.footer-home-link</code> somewhere down the line, resulting in inconsistent naming. It\'s possible that you might use <code class="inline">.home-link</code>, forget, and use it again. You may be forced to use very specific selectors in order to deal with overrides that you can\'t undo otherwise. Or you may have to use <code class="inline">!important</code> just to get your styles to work, which could end up overriding styles somewhere else on your page. In addition, lots of nesting can often lead to unreadable selectors in our CSS (ex: <code class="inline">header .nav a.home</code>). With BEM, we\'ll move some of the complexity from the CSS to the HTML.</p>\n\n<p class="new">In most cases, HTML is much easier to read than CSS. By making our HTML slightly more detailed (specifically the class names), we can make our CSS more readable and manageable.</p>')
	section.save()

	section = Section(post=post,
		number='2',
		heading='Introducing the BEM methodology',
		content='<p><a href="http://getbem.com/" class="text-link" target="_blank">BEM</a> stands for Block Element Modifier. It is a methodology/naming convention for our classes. Essentially, it gives every piece of HTML a consistent and descriptive class name, so each <strong>element</strong> (or <strong>modified-element</strong>) can be easily related to a larger <strong>block</strong>.</p>\n\n<p class="new">Think of a large jigsaw puzzle. It can be difficult to keep track of tiny pieces, but once you connect a few of them to make part of the picture, it\'s a lot easier to keep track of the parts.</p>\n\n<p>BEM has a couple of <a href="https://en.bem.info/method/naming-convention/" class="text-link" target="_blank">variants</a>. Until recently, I actually didn\'t even know I was using BEM. It turns out that the variant I use is by <a href="https://twitter.com/csswizardry" class="text-link" target="_blank">Harry Roberts</a> (who also happens to be the creator of ITCSS -- more on this in a future post). The general idea is as follows:</p>\n\n<pre><code class="language-scss">\n.block {}\n.block__element {}\n.block__element--modifier {}\n</code></pre>\n\n<p class="btw">To use more than one word for any part of the naming, use a hyphen. Example: <code class="inline">.header__social-btn--twitter</code>.<br><br>If you have nested elements like in <code class="inline">.block__elem__elem2</code>, do <code class="inline">.block__elem2</code> instead. Couple each element to the block, not its parent element.</p>\n\n<p>The goal is to split our page into <strong>blocks</strong>. Inside each block, we have <strong>elements</strong> and possibly elements with <strong>modifiers</strong> that are contextually coupled to their parent block. The result is that we no longer need to nest our selectors and don\'t have to deal with possible overrides due to specificity.</p>')
	section.save()

	section = Section(post=post,
		number='3',
		heading='Applying BEM to our example',
		content='<p>Let\'s transform our previous example into markup that follows the BEM methodology.</p>\n\n<pre><code class="language-markup">\n&lt;header class="header">\n\n  &lt;div class="header__nav-container">\n    &lt;a class="header__nav header__nav--home">Home&lt;/a>\n    &lt;a class="header__nav header__nav--about">About&lt;/a>\n    &lt;a class="header__nav header__nav--blog">Blog&lt;/a>\n  &lt;/div> &lt;!-- .header__nav-container -->\n\n  &lt;div class="header__greeting-wrapper">\n    &lt;p class="header__greeting">Hey you!&lt;/p>\n  &lt;/div> &lt;!-- .header__greeting-wrapper -->\n  \n  &lt;button class="header__cta">\n    &lt;p class="header__cta-msg">Click here!&lt;/p>\n  &lt;/button> &lt;!-- button.header__cta -->\n\n&lt;/header> &lt;!-- header.header -->\n\n&lt;footer class="footer">\n  &lt;a class="footer__nav footer__nav--home">Back Home&lt;/a>\n  &lt;a class="footer__nav footer__nav--about">More About Us&lt;/a>\n&lt;/footer> &lt;!-- footer.footer -->\n</code></pre>\n\n<p class="btw">I don\'t believe comments are part of the BEM methodology, but I learned to add comments whenever an element contains nested element(s).<br><br>If the element is a div: <br><code class="inline">&lt;-- .class.class2#id#id2 --></code><br> For elements other than divs: <br><code class="inline">&lt;-- element.class#id --></code><br><br>I find that this it helps with readability, especially with a large parent element.</p>\n\n<p class="new">Wrappers and containers are essentially interchangeable. Semantically, a <code class="inline">wrapper</code> wraps around one element, and a <code class="inline">container</code> contains multiple elements.</p>\n\n<p class="btw">I\'m not too sure about the convention for containers and wrappers. I found that attaching them with a hyphen works well for me.</p>\n\n<p>We split our HTML into two blocks: <code class="inline">.header</code> and <code class="inline">.footer</code>. Looking specifically at the latter, we see two <code class="inline">.footer__nav</code> elements, and each element has a modifier (ex: <code class="inline">.footer__nav--home</code>). Now take a look at the CSS we get when styling our navigation links.</p>\n\n<pre><code class="language-scss">\n.header__nav {} //Applies to all header nav links\n\n/* Affects specific nav link in header */\n.header__nav--home {}\n.header__nav--about {}\n.header__nav--blog {}\n\n.footer__nav {} //Applies to all footer nav links\n\n/* Affects specific nav link in footer */\n.footer__nav--home {}\n.footer__nav--about {}\n</code></pre>\n\n<p>The result is very readable and structured. We can easily see which elements belong to which blocks. We can also apply styles to elements of a similar type in a block and make modifications to specific elements if we want. In addition, every selector is just a single class, so there is no selector nesting and no specificity issues!</p>')
	section.save()

	if not post.title_url:
		post.title_url = slugify(post.title)
		post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_3steps_introduction'),
    ]

    operations = [
    	migrations.RunPython(load_post),
    ]