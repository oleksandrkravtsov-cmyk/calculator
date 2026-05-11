def calculator():
    print("--- Простий калькулятор на Python ---")
    
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
            # Обробка ділення на нуль
            if num2 == 0:
                return "Помилка: на нуль ділити не можна!"
            result = num1 / num2
        else:
            return "Помилка: невірна операція."

        return f"Результат: {result}"

    except ValueError:
        return "Помилка: вводьте тільки числа."

# Запуск програми
print(calculator())