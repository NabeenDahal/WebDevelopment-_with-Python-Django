from django.urls import path
from .views import HomePageView,aboutPageView,contactPageView,blogPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('blog/', blogPageView.as_view(), name='blog'),
]
