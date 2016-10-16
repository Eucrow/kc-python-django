from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
from posts.views import PostListQuerySet


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de artículos
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostListQuerySet.get_posts_by_user(user=self.request.user)

    # sobreescribimos el método get_serializer_class para que haga lo que nosotros deseamos,
    # en este caso devuelve PostSerializer si el método es POST o PostListSerializer si no.

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):   # obligamos a que se guarde la foto con el usuario que
                                            # está autenticado cuando se está creando una nueva
        return serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de artículos
    """
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostListQuerySet.get_posts_by_user(user=self.request.user)

    def perform_create(self, serializer):  # obligamos a que se guarde la foto con el usuario que está autenticado
                                           # cuando se está actualizando una foto
        return serializer.save(owner=self.request.user)

