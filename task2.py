# Задача 2. Работа с текущим временем и датой

from datetime import datetime
import pandas as pd

now = datetime.now()

print(f"Сегодня: {now.date()}")
print(f"Время: {now.time().strftime('%H:%M:%S')}")
print(f"День недели: {pd.Timestamp(now).day_name()}")
print(f"Номер недели в году: {now.isocalendar()[1]}")
