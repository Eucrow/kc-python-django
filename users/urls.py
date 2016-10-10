from users.views import login, logout
from django.conf.urls import url
from users.api import UserListAPI, UserDetailAPI

urlpatterns = [
    #web urls
    url(r'^login$', login),
    url(r'^logout$', logout),

    #api urls
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail')
]