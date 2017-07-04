from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from tagging.fields import TagField
#from tinymce.models import HTMLField

#from django.urls import reverse
from django.core.urlresolvers import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

#from tagging.registry import register
#from taggit.managers import TaggableManager

"""class BlogAuthor(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")

    def __str__(self):
        return self.user.username
        """

"""class Catagories(models.Model):
    catagori_name=models.CharField(max_length=30)
    Description=models.TextField()

    def __str__(self):
        return self.catagori_name"""


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
        self).get_queryset()\
        .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    text = RichTextUploadingField()
    tags = TagField()
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.SET_NULL,null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects=models.Manager()
    published = PublishedManager()



    #tags=TaggableManager()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ["-publish", ]




#register(Post)