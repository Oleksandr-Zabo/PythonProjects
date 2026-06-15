from django.http import JsonResponse
import random

PREDICTIONS = [
    "На вас чекає несподівана радість.",
    "Сьогодні буде чудовий день для нових починань.",
    "Будьте відкриті до нових можливостей, вони вже близько.",
    "Ваша праця буде винагороджена.",
    "Знайдіть час для відпочинку, це важливо.",
    "Довіряйте своїй інтуїції.",
    "Незабаром ви отримаєте приємні новини.",
    "Подорож принесе вам нові враження.",
    "Ваші мрії почнуть збуватися.",
    "Зосередьтеся на своїх цілях, і ви досягнете успіху.",
    "Сміливість відкриє нові двері.",
    "Не бійтеся змін, вони на краще.",
    "Хтось думає про вас з теплом.",
    "Ваша доброта повернеться до вас сторицею.",
    "Навчіться чогось нового сьогодні.",
    "Маленькі кроки ведуть до великих звершень.",
    "Поділіться своєю радістю з іншими.",
    "Слухайте своє серце.",
    "Удача посміхнеться вам у найнесподіваніший момент.",
    "Ваше терпіння буде винагороджено.",
    "На вас чекає цікава зустріч.",
    "Будьте вдячні за те, що маєте.",
    "Сьогодні ви знайдете відповідь на важливе питання.",
    "Не забувайте про своїх близьких.",
    "Ваш оптимізм заразливий.",
    "Настав час для творчості.",
    "Ви здатні на більше, ніж думаєте.",
    "Зробіть щось приємне для себе.",
    "Ваша енергія приваблює успіх.",
    "Світ чекає на ваші ідеї.",
]

# 1
def get_prediction(request):
    """
    Returns a random prediction from the list as a JSON response.
    """
    prediction = random.choice(PREDICTIONS)
    return JsonResponse({'prediction': prediction})

# 2
def get_random_number(request):
    # Generate a random integer using 16 bits (roughly 0 to 65,535) - not 32-bit because > int in GraphQL
    random_n = random.getrandbits(16)
    return JsonResponse({'random_n': random_n})

def get_random_by_range(request, start=0, end=100):
    # Генеруємо випадкове число в діапазоні [start, end]
    random_n = random.randint(start, end)
    return JsonResponse({'random_n': random_n})
def get_random_numbers(request, start=0, end=100, count=5):
    # Генеруємо список випадкових чисел у діапазоні [start, end]
    random_list = [random.randint(start, end) for _ in range(count)]
    return JsonResponse({'random_numbers': random_list})
