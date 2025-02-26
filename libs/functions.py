


from collections import OrderedDict
from datetime import timedelta, date, datetime


is_dict = lambda var: isinstance(var, (dict, OrderedDict))


def get_month():
    today = date.today() + timedelta(days=1)
    first_day_1 = date(today.year, today.month, 1)
    last_month = first_day_1 - timedelta(days=20)
    first_day_2 = date(last_month.year, last_month.month, 1)
    last_month = first_day_2 - timedelta(days=20)
    first_day_3 = date(last_month.year, last_month.month, 1)
    return (first_day_1, today), (first_day_2, first_day_1), (first_day_3, first_day_2)



def get_days_in_month(date):
    # Получаем первый день следующего месяца
    next_month = date.replace(day=28) + timedelta(days=4)  # Переход на следующий месяц
    first_day_next_month = next_month.replace(day=1)  # Первый день следующего месяца
    last_day_of_month = first_day_next_month - timedelta(days=1)  # Последний день текущего месяца

    # Генерируем список всех дней месяца
    days_in_month = []
    for day in range(1, last_day_of_month.day + 1):
        days_in_month.append(date.replace(day=day))

    return days_in_month



def generate_date_list(start_date, end_date=None, weekends=True) -> list:
   if end_date is None:
       end_date = datetime.today().date()
   
   
   if isinstance(start_date, str):
       start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
   if isinstance(end_date, str):
       end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
   
   # Создаем список дат
   date_list = []
   
   # Проверяем порядок дат
   if start_date > end_date:
       return date_list
   
   
   current_date = start_date
   while current_date <= end_date:
       # Проверяем, что день не суббота (5) и не воскресенье (6)
       if weekends or current_date.weekday() < 5:
           date_list.append(current_date)
       current_date += timedelta(days=1)
   return date_list




def group_by(list: dict | OrderedDict, field: str, is_unique: bool = False) -> OrderedDict:
    new_list = OrderedDict()
    for element in list:
        if is_dict(element):
            key = element[field]
        if not is_unique:
            if key not in new_list:
                new_list[key] = []
            new_list[key].append(element)
        else:
            new_list[key].append(element)
    return new_list
