from django.shortcuts import render
from .decorators import permission_required
from .models import AccessControl


@permission_required('access_system')
def access_table_view(request):
    access_controls = AccessControl.objects.all()
    return render(request, 'access_control/access_table.html', {'access_controls': access_controls})
