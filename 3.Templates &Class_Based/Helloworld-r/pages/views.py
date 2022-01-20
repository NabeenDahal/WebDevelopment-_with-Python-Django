# pages/views.py
from django.views.generic import TemplateView #new

class HomePageView(TemplateView):
    template_name = 'home.html' 

class aboutPageView(TemplateView):
    template_name = 'about.html' 

class contactPageView(TemplateView):
    template_name = 'contact.html' 

class blogPageView(TemplateView):
    template_name = 'blog.html' 