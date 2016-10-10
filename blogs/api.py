from django.contrib.auth.models import User
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from blogs.serializers import BlogSerializer


class BlogListAPI(APIView):
    """
    Endpoint de listado de blogs
    """

    def get(self, request):
        blogs = User.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
