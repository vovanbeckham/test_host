import datetime
from django.db.models import Sum


from libs.functions import generate_date_list, get_days_in_month, get_month, group_by
from manicure.models import ProvidedService


def get_data_service():
    dates = get_month()
    data_list = []
    for date in dates:
        data = []
        label = []
        sum = 0
        data_month = ProvidedService.objects.filter(
            date__gte=date[0],
            date__lt=date[1]
            ).values(
                'service__short', 
                'service__base__name'
                ).annotate(Sum('price')).order_by('-price__sum')
        
    
        for service in data_month:
            label.append('%s %s' % (
                service['service__base__name'], 
                service['service__short']
                ))
            data.append(float(service['price__sum']))
            sum += service['price__sum']
        if data:
            data_list.append({'month': date[0], 'data': data, 'label': label, 'sum': float(sum)})

    return data_list



def get_data_dates_service(date_month):
    data_list = []
    all_dates = get_days_in_month(datetime.date(date_month.year, date_month.month, 1))
    data_month = ProvidedService.objects.filter(
        date__gte=all_dates[0],
        date__lte=all_dates[-1]
        ).values( 
            'date'
            ).annotate(Sum('price'))
    data_month = group_by(data_month, "date")

    data = []
    label = []
    sum = 0
    for date in all_dates:
        if date in data_month:
            _sum = 0
            for element in data_month[date]:
                _sum += element["price__sum"]
            label.append(str(date.day))
            data.append(float(_sum))
            sum += _sum
        else:
            label.append(str(date.day))
            data.append(float(0))
    
    data_list.append({'month': all_dates[0], 'data': data, 'label': label, 'sum': float(sum)})

    return data_list