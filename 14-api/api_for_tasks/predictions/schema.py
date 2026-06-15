import random
import graphene

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

class Query(graphene.ObjectType):
    random_prediction = graphene.String()
    random_number = graphene.Int()
    random_number_by_range = graphene.Int(start=graphene.Int(), end=graphene.Int())
    random_numbers = graphene.List(graphene.Int, start=graphene.Int(), end=graphene.Int(), count=graphene.Int())

    def resolve_random_prediction(root, info):
        return random.choice(PREDICTIONS)

    def resolve_random_number(root, info):
        return random.getrandbits(32)

    def resolve_random_number_by_range(root, info, start=0, end=100):
        return random.randint(start, end)

    def resolve_random_numbers(root, info, start=0, end=100, count=5):
        return [random.randint(start, end) for _ in range(count)]
