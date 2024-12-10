from functools import wraps
from django.http import HttpResponseForbidden
from .utils import has_permission


def permission_required(view_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not has_permission(request.user, view_name):
                return HttpResponseForbidden("У вас нет доступа к этому ресурсу.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
