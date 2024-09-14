# Задача 4. Опции и флаги
import argparse

parser = argparse.ArgumentParser(description="Скрипт принимает число и строку")

parser.add_argument('num', type=int, help='Число(целое)')
parser.add_argument('string', type=str, help='Строка')
parser.add_argument('--verbose', action='store_true', help='Дополнительная информация')
parser.add_argument('--repeat', type=int, default=1, help='Сколько раз повторить строку (по умолчанию 1)')

args = parser.parse_args()

if args.verbose:
    print(f"[INFO] Число: {args.num}")
    print(f"[INFO] Строка: {args.string}")
    print(f"[INFO] Повторение строки {args.repeat} раз(а)")

for i in range(args.repeat):
    print(f"{i+1}: {args.string}")

# Строка для примера в cmd:
# python3 Task4.py 42 "Hello world!" --verbose --repeat 4