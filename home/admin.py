from home.models import upload_blog
from django.contrib import admin

# Register your models here.
class Blog(admin.ModelAdmin):
     search_fields = ('blog_title',)
     list_display = ('blog_title','blog_author','blog_uploaded_at','blog_updated_at')
     list_filter = ('blog_author', 'blog_uploaded_at')


admin.site.register(upload_blog,Blog)