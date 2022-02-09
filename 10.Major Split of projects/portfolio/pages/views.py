from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# from .models import Homepage

def home(request):
    # homepage = Homepage.objects.all()
    # context = {
    #     'title' : homepage[0].title,
    #     'paragraph_1' : homepage[0].paragraph_1,
    #     'paragraph_2' : homepage[0].paragraph_2,
    #     'header_image' : homepage[0].header_image,
    #     'skill_1' : homepage[0].skill_1,
    #     'skill_2' : homepage[0].skill_2,
    #     'tools' : homepage[0].tools
    # }
    return render( request,'pages/home.html')


class about(TemplateView):
    template_name = 'pages/about.html' 

class contact(TemplateView):
    template_name = 'pages/contact.html' 

class blog(TemplateView):
    template_name = 'blogs/blogs.html' 
