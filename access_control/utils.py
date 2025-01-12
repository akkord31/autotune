from .models import AccessControl


def has_permission(user, view_name):
    try:
        access = AccessControl.objects.get(user=user)
        permission_map = {
            'homepage': access.view_homepage, #
            'about': access.view_about,
            'services': access.view_services, #
            'suppliers': access.view_suppliers, #
            'employees': access.view_employees, #
            'salary': access.view_salary,
            'reports': access.view_reports, #
            'access_system': access.view_access_system, #
            'archive': access.view_archive, #
        }

        return permission_map.get(view_name, 0) in [1, 2]  # 1 - доступ разрешен, 0 - доступ запрещен
    except AccessControl.DoesNotExist:
        return False

