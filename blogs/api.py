from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from blogs.serializers import BlogSerializer



class BlogListAPI(ListCreateAPIView):
    """
    Endpoint de listado de blogs
    """

    queryset = User.objects.all()
    serializer_class = BlogSerializer
