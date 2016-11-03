from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer
from posts.views import PostListQuerySet


# TODO: convert this in a ViewSet (video Día 6 - Sesión 2 Autorización, Autenticación, Filtrado de da.flv, 1:25

class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de artículos
    """
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (PostPermission,)

    def get_queryset(self):

        posts_by_user = PostListQuerySet.get_posts_by_user(user=self.request.user)

        # filter by search
        search = self.request.query_params.get('search', None)

        if search is not None:
            queryset = posts_by_user.filter(title__icontains=search)

        #order by title
        title = self.request.query_params.get('title', None)
        if title == "asc":
            by_title = "title"
        elif title == "des":
            by_title = "-title"

        if title is not None:
            queryset = queryset.order_by(by_title)
        
        # order by title
        date =self.request.query_params.get('date', None)
        by_date = ""
        if date == "asc":
            by_date = "publication_date"
        elif date == "des":
            by_date = "-publication_date"

        if date is not None:
            queryset = queryset.order_by(by_date)

        return queryset

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
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (PostPermission,)

    def get_queryset(self):
        return PostListQuerySet.get_posts_by_user(user=self.request.user)

    def perform_update(self, serializer):  # obligamos a que se guarde la foto con el usuario que está autenticado
                                           # cuando se está actualizando una foto
        return serializer.save(owner=self.request.user)

