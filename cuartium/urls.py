"""cuartium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from posts.views import Home, PostDetail, PostCreationView
from users.views import login, logout
from categories.views import home as categories_home
from blogs.views import Blog

urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', login),
    url(r'^logout$', logout),
    url(r'^posts/(?P<pk>[0-9]+)$', PostDetail.as_view(), name='post_detail'),
    url(r'^newpost$', PostCreationView.as_view()),
    url(r'^categories$', categories_home),
    url(r'^blogs/(?P<user_blog>.+)$', Blog.as_view()),
]
