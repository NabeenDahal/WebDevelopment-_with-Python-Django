#config/urls.py

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('api/',include('api.urls')) #new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#api/urls.py
from django.urls import path
from .views import BlogAPIView,BlogDetailAPIView

urlpatterns = [
    path('', BlogAPIView.as_view()),
    path('<int:pk>', BlogDetailAPIView.as_view()),
]