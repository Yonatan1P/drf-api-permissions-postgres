from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Post
from .permissions import IsAuthororReadOnly
from .serializers import PostSerializer

class PostsList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

