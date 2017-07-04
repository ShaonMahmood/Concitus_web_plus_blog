from django import template

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


"""
to use this template tag just load
{% load blog_tags %} on top of any template

syntex: {% total_posts %},
{% show_latest_posts 3 %}"""