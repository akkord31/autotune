from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from access_control.decorators import permission_required
from services.models import Car, Service
from .models import ServiceArchive


@permission_required('archive')
def archive_add(request):
    if request.method == 'POST':
        car_code = request.POST.get('car_code')
        service_code = request.POST.get('service_code')
        service_date = request.POST.get('service_date')

        try:
            car = Car.objects.get(code=car_code)
            service = Service.objects.get(code=service_code)

            final_price = service.price * car.coefficient

            service_archive = ServiceArchive(
                car=car,
                service=service,
                service_date=service_date,
                final_price=final_price
            )
            service_archive.save()

            return redirect('archive')

        except (Car.DoesNotExist, Service.DoesNotExist):
            return HttpResponse("Ошибка: Неверные данные!", status=400)

    return render(request, 'archive/archive.html')


@permission_required('archive')
def archive_view(request):
    archive_records = ServiceArchive.objects.all()

    if 'car_code' in request.GET and request.GET['car_code']:
        archive_records = archive_records.filter(car__code=request.GET['car_code'])

    if 'service_code' in request.GET and request.GET['service_code']:
        archive_records = archive_records.filter(service__code=request.GET['service_code'])

    if 'start_date' in request.GET and request.GET['start_date']:
        archive_records = archive_records.filter(service_date__gte=request.GET['start_date'])

    if 'end_date' in request.GET and request.GET['end_date']:
        archive_records = archive_records.filter(service_date__lte=request.GET['end_date'])

    sort_by = request.GET.get('sort_by', 'service_date')
    if sort_by in ['service_date', 'final_price', 'car__code', 'service__code', 'service__name', 'car__brand', 'car__coefficient']:
        archive_records = archive_records.order_by(sort_by)

    return render(request, 'archive/archive.html', {'archive_records': archive_records})
