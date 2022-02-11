from rest_framework import generics,permissions
from blog.models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly # new



class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer