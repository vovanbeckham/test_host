
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages

from manicure.functions import get_data_dates_service, get_data_service




def index(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    service_dict = get_data_service()


    return render(request, "manicure/index.html", locals())


def by_services(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    service_dict = get_data_service()


    return render(request, "manicure/by_services.html", locals())




def by_dates(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    months = [
        ('1', 'Январь'),
        ('2', 'Февраль'),
        ('3', 'Март'),
        ('4', 'Апрель'),
        ('5', 'Май'),
        ('6', 'Июнь'),
        ('7', 'Июль'),
        ('8', 'Август'),
        ('9', 'Сентябрь'),
        ('10', 'Октябрь'),
        ('11', 'Ноябрь'),
        ('12', 'Декабрь'),
    ]

    selected_month = request.GET.get('month')
    today = datetime.today()
    service_dict = get_data_dates_service(today)
    print(service_dict)
    print("HERE")
    return render(request, "manicure/by_dates.html", locals())