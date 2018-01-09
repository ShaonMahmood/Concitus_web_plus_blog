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
    slug = models.SlugField(max_length=500)
    text = RichTextUploadingField()
    tags = TagField()
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.SET_NULL,null=True)
    home_image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    excerpt_text = models.CharField(max_length=1000, blank=True)
    total_viewed = models.IntegerField(default=0)
    publish_time = models.DateTimeField(
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(
        blank=True,
        null=True
    )
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
                       args=[self.pk,
                             self.slug])

    class Meta:
        ordering = ["-created", ]




#register(Post)