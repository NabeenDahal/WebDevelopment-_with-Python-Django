from django.urls import path
# from .views import homePageView, djangoView,contactView,about
from .views import home,about,contact,blog

urlpatterns = [
    path('', home, name='home'),
    path('about/', about.as_view(), name='about'),
    path('contact/', contact.as_view(), name='contact'),
    path('blogs/', blog.as_view(), name='blogs'),
]