from django.shortcuts import render, redirect
from posts.models import Post



def blog(request, user_p):
    """
    User blog view
    :param request: httpRequest
    :return: httpResponse
    """

    possible_posts = Post.objects.filter(owner_exact=user_p)
    context = {'posts_list': possible_posts}
    return render(request, 'blogs/home.html', context)

    #else:
    #    context = "Ese usuario no existe"
    #    return render(request, 'categories/', context)
