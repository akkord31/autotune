from django.shortcuts import render

from access_control.decorators import permission_required
from .models import ServiceArchive


@permission_required('archive')
def archive_view(request):
    archive_records = ServiceArchive.objects.all()
    return render(request, 'archive/archive.html', {'archive_records': archive_records})
