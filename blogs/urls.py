from blogs.views import Blog, BlogList
from django.conf.urls import url

urlpatterns = [
    url(r'^blogs/(?P<user_blog>.+).html$', Blog.as_view()),
    url(r'^blogs', BlogList.as_view()),
]