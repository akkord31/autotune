from django.shortcuts import render
from access_control.decorators import permission_required


def homepage_view(request):
    return render(request, 'homepage/menu.html')


@permission_required('about')
def about_us_view(request):
    return render(request, 'homepage/about_us.html')
