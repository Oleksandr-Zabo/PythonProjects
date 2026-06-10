from django.shortcuts import render
import datetime

def show_day(request):
    days = {
        0: ("Понеділок", "monday.webp"),
        1: ("Вівторок", "tuesday.webp"),
        2: ("Середа", "wednesday.webp"),
        3: ("Четвер", "thursday.webp"),
        4: ("П'ятниця", "friday.webp"),
        5: ("Субота", "saturday.webp"),
        6: ("Неділя", "sunday.jpg"),
    }

    today = datetime.datetime.today().weekday()  # 0 = Monday
    day_name, image = days[today]

    return render(request, 'weekapp/day.html', {
        'day_name': day_name,
        'image': image
    })
