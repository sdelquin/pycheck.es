from functools import wraps

from django.conf import settings
from django.http import JsonResponse

from core.models import AuthToken, Student

catalog = {}


def api_method(func):
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


@api_method
def version(request):
    """Devuelve la versión actual de la API."""
    return settings.API_VERSION


@api_method
def index(request):
    """Versión y catálogo de llamadas disponibles."""
    return {
        'version': settings.API_VERSION,
        'catalog': catalog,
    }


@api_method
def login(request):
    username = request.POST.get('username')
    password_hash = request.POST.get('password_hash')
    student = Student.load_by_username(username)
    if student and student.check_password(password_hash):
        token = AuthToken.issue_token_for_student(student)
        return token
    raise ValueError('El username {username} no existe')
