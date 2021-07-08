from django.db import models

# Create your models here.
class upload_blog(models.Model):
     blog_title = models.CharField(max_length=300)
     blog_author = models.CharField(max_length=100)
     image = models.ImageField(upload_to="upload/media", default="static/img/hero-bg.jpg")
     blog_category = models.CharField(max_length=200 , default="undefined")
     blog_content = models.TextField(max_length=50000)
     blog_uploaded_at = models.DateTimeField(auto_now_add=True)
     blog_updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.blog_title
