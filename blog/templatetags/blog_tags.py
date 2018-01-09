from bs4 import BeautifulSoup
from django import template

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish_time')[:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/popular_posts.html')
def show_popular_posts(count=5):
    popular_posts = Post.published.order_by('-total_viewed',)[:count]
    return {'popular_posts': popular_posts}

@register.filter
def image_url_finder(value):
    soup=BeautifulSoup(value,'html.parser')
    images=soup.find_all('img')
    if images:
        imageUrl=images[0].get('src')
        return imageUrl
    return None


def get_next_at(_str, at, f=2, b=10):
    if _str[at] == " ":
        return at
    f_at, b_at = at, at
    while f:
        f_at += 1
        f -= 1
        try:
            if _str[f_at] == " ": return f_at
        except IndexError:
            return f_at - 1
    while b:
        b_at -= 1
        b -= 1
        try:
            if _str[b_at] == " ": return b_at
        except IndexError:
            pass
    return at

@register.filter
def smart_excerpt(quote, length=0):
    length = (length if length > 0 else 90)
    if len(quote) > length:
        length = get_next_at(quote, length - 3)
        quote = quote[:length] #+ '...'
    return quote


@register.filter(name='times')
def times(number):
    if number is None:
        return []
    return range(1, number+1)

"""
to use this template tag just load
{% load blog_tags %} on top of any template

syntex: {% total_posts %},
{% show_latest_posts 3 %}"""