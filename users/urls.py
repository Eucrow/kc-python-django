from users.views import login, logout
from django.conf.urls import url

urlpatterns = [
    url(r'^login$', login),
    url(r'^logout$', logout),
]