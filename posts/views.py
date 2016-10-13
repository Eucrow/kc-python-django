from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from time import localtime, strftime

from posts.forms import PostCreationForm
from posts.models import Post

from django.urls import reverse


class Home(View):
    def get(self, request):
        """
        Renderiza el home con un listado de posts
        Args:
            request: objeto httpRequest con los datos de la petición
        Returns: objeto HttpResponse con los datos de la respuesta

        """
        # recupera todos los posts de la base de datos
        date_now = strftime("%Y-%m-%d", localtime())
        time_now = strftime("%H:%M:%S", localtime())
        posts = Post.objects.all().filter(Q(publication_date=date_now, publication_time__gte=time_now) | Q(publication_date__gt=date_now)).order_by('-created_at')
        context = {'posts_list': posts}
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


class PostCreationView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Method get to create a new post
        :param request: HttpRequest object
        :return: HttpResponse object with the response
        """
        message = None
        post_form = PostCreationForm()
        context = {'form': post_form, 'message': message}
        return render(request, 'posts/post_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
       Presenta el formuario para crear un post y en el caso de que la petición sea post la valida
       y la crea en el caso de que sea válida
       Args:
       request:
       returns:
       """
        message = None
        post_with_user = Post(owner=request.user)
        post_form = PostCreationForm(request.POST, instance=post_with_user)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostCreationForm()  # vaciamos el formulario
            message = 'Artículo creado satisfactoriamente <a href="{0}">Ver artículo</a>'.format(
                reverse('post_detail', args=[new_post.pk])
            )

        context = {'form': post_form, 'message': message}
        return render(request, 'posts/post_creation.html', context)
