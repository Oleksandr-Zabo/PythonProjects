from datetime import date, timedelta

from django.shortcuts import render
from django.utils import timezone


def current_datetime_view(request):
    now = timezone.localtime()
    context = {"current_datetime": now}
    return render(request, "feachers/current_datetime.html", context)


def multiplication_table_view(request):
    numbers = list(range(1, 11))
    table = [[row * col for col in numbers] for row in numbers]
    context = {"numbers": numbers, "table": table}
    return render(request, "feachers/multiplication_table.html", context)
#use templates -> multiplication_table.html

def programmer_day_view(request):
    current_year = timezone.localdate().year
    programmer_day = date(current_year, 1, 1) + timedelta(days=255)
    context = {
        "current_year": current_year,
        "programmer_day": programmer_day,
    }
    return render(request, "feachers/programmer_day.html", context)

