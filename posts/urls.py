from posts.views import PostDetail, PostCreationView
from django.conf.urls import url

urlpatterns = [
    url(r'^posts/(?P<pk>[0-9]+)$', PostDetail.as_view(), name='post_detail'),
    url(r'^newpost$', PostCreationView.as_view()),
]