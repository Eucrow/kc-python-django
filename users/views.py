from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect, render


def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    Args:
        request: objeto httpRequest con los datos de la petición
    Returns: objeto HttpResponse con los datos de la respuesta

    """
    error_message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_message = "Usuario o contraseña incorrecta"
        else:
            if user.is_active:
                # le decimos que el usuario user está autenticado para las siguientes peticiones que haga
                django_login(request, user)
                return redirect('/')
            else:
                error_message = "Cuenta de usuario inactiva"

    return render(request, 'users/login.html', {'error': error_message})
