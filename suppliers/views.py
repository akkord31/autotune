from django.shortcuts import render

from access_control.decorators import permission_required
from .models import Supplier


@permission_required('suppliers')
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})
