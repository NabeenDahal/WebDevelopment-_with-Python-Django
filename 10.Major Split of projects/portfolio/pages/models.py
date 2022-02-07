from django.db import models


class Homepage(models.Model):
    title = models.CharField(max_length=150)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    skill_1 =models.CharField(max_length=150)
    skill_2 = models.CharField(max_length=150)
    tools = models.CharField(max_length=150)
     
