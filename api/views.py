from functools import wraps

from django.conf import settings
from django.http import JsonResponse

from core.models import AuthToken, Student

catalog = {}


def is_api(func):
    @wraps(func)
    def inner_function(request, *args, **kwargs):
        response = {
            'status': 'error',
        }
        try:
            response['result'] = func(request, *args, **kwargs)
            response['status'] = 'ok'
        except Exception as err:
            response['message'] = str(err)
        finally:
            return JsonResponse(response)

    if hasattr(func, '__name__'):
        catalog[func.__name__] = func.__doc__ or 'Falta documentación'
    return inner_function


@is_api
def version(request):
    """Devuelve la versión actual de la API."""
    return {
        'version': settings.API_VERSION,
    }


@is_api
def index(request):
    """Versión y catálogo de llamadas disponibles."""
    return {
        'version': settings.API_VERSION,
        'catalog': catalog,
    }


@is_api
def login(request):
    username = request.POST.get('username')
    password_hash = request.POST.get('password_hash')
    student = Student.load_by_username(username)
    if student and student.check_password(password_hash):
        token = AuthToken.issue_token_for_student(student)
        return token
    raise ValueError('El username {username} no existe')
