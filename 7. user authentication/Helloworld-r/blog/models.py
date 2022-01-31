# blog/models.py
from django.db import models
from django.urls import reverse #new

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)  #ForeignKey allows many-to-one relationships between models , this means a author can have many blog posts
    body = models.TextField()
    # description = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    subtitle = models.CharField(max_length=200,null=True)

    def get_absolute_url(self): # add this method
        return reverse('blog_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
