from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de artículos
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de artículos
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
