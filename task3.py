# Задача 3. Планирование задач

from datetime import datetime, timedelta


def future_date(days):
    now = datetime.now().date()
    return now + timedelta(days=days)


# Примеры:
print(future_date(5))
print(future_date(10))
print(future_date(-5))
