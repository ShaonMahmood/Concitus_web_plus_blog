from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_time','created','status')
    list_filter = ('status', 'created', 'publish_time', 'author')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['status', 'created']

# Register your models here.

admin.site.register(Post,PostAdmin)

