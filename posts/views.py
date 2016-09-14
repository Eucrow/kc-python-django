from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from posts.models import Post


class Home(View):
    def get(self, request):
        """
        Renderiza el home con un listado de fotos
        Args:
            request: objeto httpRequest con los datos de la petición
        Returns: objeto HttpResponse con los datos de la respuesta

        """
        # recupera todos los posts de la base de datos
        posts = Post.objects.all().order_by('-created_at')
        context = {'posts_list': posts[:4]}
        return render(request, 'posts/home.html', context)

class PostDetail(View):
    def get(self, request, pk):
        """
        Recupera el detalle del post
        :param request: objeto httpRequest con los datos de la petición
        :return: objeto httpResponse con los datos de la respuesta
        """
        possible_post = Post.objects.filter(pk=pk).select_related("owner")
        if len(possible_post) == 0:
            return HttpResponseNotFound("Ese post que buscas no existe")
        elif len(possible_post) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        post = possible_post[0]
        context = {'post': post}
        return render(request, 'posts/post_detail.html', context)




