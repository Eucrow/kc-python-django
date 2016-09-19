from blogs.views import Blog
from django.conf.urls import url

urlpatterns = [
    url(r'^blogs/(?P<user_blog>.+)$', Blog.as_view()),
]