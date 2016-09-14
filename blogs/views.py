from django.shortcuts import render
from django.views import View

from posts.models import Post
from django.contrib.auth.models import User


class Blog(View):

    def get(self, request, user_blog): #sobreescribimos el método get_queryset
        """
        Renderiza el blog de un usuario con un listado de sus posts
        :param request: objeto HttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        posts_queryset = Post.objects.filter(owner__username=user_blog).select_related('owner')
        context = {'posts_list': posts_queryset}
        return render(request, 'blogs/blog.html', context)
