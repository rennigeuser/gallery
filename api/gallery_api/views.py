from rest_framework import generics
from apps.gallery.models import Image, Like, Post
from .serializers import PostSerializer, ImageSerializer
from rest_framework import permissions


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

post_list = PostListView.as_view()


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

post_create = PostCreateView.as_view()


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        return Post.objects.get(pk=self.kwargs['pk'])

post_detail = PostDetailView.as_view()


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Post.objects.get(pk=self.kwargs['pk'])

post_delete = PostDeleteView.as_view()


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

image_list = ImageListView.as_view()