# middleware.py
from .models import AccessControl


class AccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                access = AccessControl.objects.get(user=request.user)
                request.permissions = {
                    'view_about': access.view_about,
                    'view_reports': access.view_reports,
                    'view_services': access.view_services,
                    'view_access_system': access.view_access_system,
                    'view_suppliers': access.view_suppliers,
                    'view_employees': access.view_employees,
                    'view_salary': access.view_salary,
                }
            except AccessControl.DoesNotExist:
                request.permissions = {}
        else:
            request.permissions = {}

        response = self.get_response(request)
        return response
