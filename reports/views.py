from django.shortcuts import render
from django.http import HttpResponse

from access_control.decorators import permission_required
from archive.models import ServiceArchive
from datetime import datetime


@permission_required('reports')
def generate_report(request):
    total_amount = 0
    min_amount = None
    max_amount = None
    avg_amount = None
    start_date = None
    end_date = None
    records = None

    if request.GET.get('start_date') and request.GET.get('end_date'):
        try:
            start_date = datetime.strptime(request.GET['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(request.GET['end_date'], '%Y-%m-%d').date()

            records = ServiceArchive.objects.filter(
                service_date__gte=start_date,
                service_date__lte=end_date
            )

            if records:
                total_amount = sum(record.final_price for record in records)
                min_amount = min(record.final_price for record in records)
                max_amount = max(record.final_price for record in records)
                avg_amount = total_amount / len(records)

        except ValueError:
            return HttpResponse("Ошибка: Неверный формат даты!", status=400)

    return render(request, 'reports/reports.html', {
        'records': records,
        'total_amount': total_amount,
        'min_amount': min_amount,
        'max_amount': max_amount,
        'avg_amount': avg_amount,
        'start_date': start_date,
        'end_date': end_date
    })
