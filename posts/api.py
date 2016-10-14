from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de artículos
    """

    queryset = Post.objects.all()

    # sobreescribimos el método get_serializer_class para que haga lo que nosotros deseamos,
    # en este caso devuelve PostSerializer si el método es POST o PostListSerializer si no.

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de artículos
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
