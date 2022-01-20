from django.urls import path
from .views import homepageview,aboutpageview,contactpageview,blogpageview

urlpatterns = [
    path('home/', homepageview, name='home'),
    path('about/', aboutpageview, name='about'),
    path('contact/', contactpageview, name='contact'),
    path('blog/', blogpageview, name='blog'),
]
