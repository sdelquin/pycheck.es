import json
from functools import wraps

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import AuthToken, Context

catalog = {}


def api_method(func):
    @csrf_exempt
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
def status(request):
    """Devuelve el estado y versión de la API."""
    return {
        'active': True,
        'version': settings.API_VERSION,
        'timezone': settings.TIME_ZONE,
    }


@api_method
def index(request):
    """Versión y catálogo de llamadas disponibles."""
    return {
        'version': settings.API_VERSION,
        'catalog': catalog,
    }


def login_error(username, context_code):
    return ValueError(
        'Error al intentar validarse como usuario.'
        f' Puede que el código del contexto {context_code} sea inválido,'
        f' o el username {username} no es válido en ese'
        ' contexto, o la contraseña es incorrecta.'
    )


@api_method
def login(request):
    if request.method != 'POST':
        raise ValueError('Esta API solo puede ser llamada con POST')
    data = json.loads(request.body)
    context_code = data['context']
    username = data['username']
    if (context := Context.load_context_by_code(context_code)) is None:
        raise login_error(context_code, username)
    if (student := context.load_student_by_username(username)) is None:
        raise login_error(context_code, username)
    password = data['password']
    if student.validate_password(password) is False:
        raise login_error(context_code, username)
    token = AuthToken.issue_token_for_student(student)
    return token.value
