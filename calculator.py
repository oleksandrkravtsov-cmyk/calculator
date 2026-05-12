import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def calculator():
    # Get app name from .env, fallback to default if not found
    app_name = os.getenv("APP_NAME", "Простий калькулятор на Python")
    print(f"--- {app_name} ---")
    
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть дію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Помилка: на нуль ділити не можна!"
            result = num1 / num2
        else:
            return "Помилка: невірна операція."

        return f"Результат: {result}"

    except ValueError:
        return "Помилка: вводьте тільки числа."

print(calculator())
