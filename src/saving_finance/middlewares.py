from threading import local
from typing import Callable, Any, Optional

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.models import TokenUser

from apps.core.models import User

USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')

_thread_locals = local()


def _do_set_current_user(user_fun: Callable[[Any], Any]) -> None:
    setattr(_thread_locals, USER_ATTR_NAME, user_fun.__get__(user_fun, local))


def _set_current_user(user: Optional['User'] = None) -> None:
    """
    Sets current user in local thread.
    Can be used as a hook e.g. for shell jobs (when request object is not
    available).
    """
    _do_set_current_user(lambda self: user)


class ThreadLocalUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.user closure; asserts laziness;
        # memorization is implemented in
        # request.user (non-data descriptor)
        _do_set_current_user(lambda self: getattr(request, 'user', None))
        response = self.get_response(request)
        return response


def get_current_user() -> User | None:
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    if callable(current_user):
        return current_user()
    return current_user


def get_current_authenticated_user() -> User | None:
    current_user = get_current_user()
    if isinstance(current_user, (AnonymousUser, TokenUser)):
        return None
    return current_user
