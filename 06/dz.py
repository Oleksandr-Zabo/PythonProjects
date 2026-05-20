import time

#1 and #2
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@time_it
def prime_nums(start=0, end=1000):#без затримки - лише час розрахунку
    for i in range(start, end):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            print(i)

@time_it
def prime_nums_arr(start=0, end=1000):#без затримки - лише час розрахунку
    arr=[]
    for i in range(start, end):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)
    print(arr[:10]) # Виводимо лише перші 10 простих чисел для демонстрації

@time_it
def prime_nums_delay(start=0, end=1000):# Додаємо затримку для демонстрації різниці в часі
    for i in range(start, end):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
            print(i)
            time.sleep(0.01)

print("---#1---\n")
prime_nums_delay()

print("\n---#2---\n")
prime_nums(100, 20000)
prime_nums_arr(100, 40000)



#3
print("\n---#3---\n")
# Базовий декоратор для Мінфіну
def ministry_finance_decorator(report_func):
    def inner(*args, **kwargs):
        print("=== Мінфін: початок звіту ===")
        report_func(*args, **kwargs)
        print("=== Мінфін: кінець звіту ===\n")
    return inner

# Декоратор для Податкової
def tax_service_decorator(report_func):
    def inner(*args, **kwargs):
        print("<XML>")
        report_func(*args, **kwargs)
        print("</XML>\n")
    return inner

# Декоратор для Статистичної служби
def statistics_service_decorator(report_func):
    def inner(*args, **kwargs):
        print("----- Статистичний звіт -----")
        report_func(*args, **kwargs)
        print("----- Кінець статистичного звіту -----\n")
    return inner


# Приклад використання:
@ministry_finance_decorator
def financial_report(year):
    print(f"Фінансовий звіт за {year} рік.")

@tax_service_decorator
def employee_report(department):
    print(f"Звіт по відділу {department}.")

@tax_service_decorator
@statistics_service_decorator
def production_report(product):
    print(f"Звіт по виробництву: {product}.")


# Виклики
financial_report(2023)
employee_report("P35")
production_report("Металоконструкції")
