from django.urls import path
from .views import BlogListAPIView,BlogDetailAPIView,BlogCreateAPIView,BlogUpdateAPIView,BlogDeleteAPIView,BlogRetrieveAPIView

urlpatterns = [
    path('', BlogListAPIView.as_view()),
    path('<int:pk>', BlogRetrieveAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view()),
    path('update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('delete/<int:pk>', BlogDeleteAPIView.as_view()),
    path('detail/<int:pk>', BlogDetailAPIView.as_view()),
]