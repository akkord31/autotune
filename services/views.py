from django.shortcuts import render
from access_control.decorators import permission_required
from .models import Service, Car


@permission_required('services')
def services_view(request):
    services = Service.objects.all()
    cars = Car.objects.all()
    return render(request, 'services/services.html', {'services': services, 'cars': cars})
