def calculator():
    print("--- Простой калькулятор на Python ---")
    
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите действие (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Обработка деления на ноль
            if num2 == 0:
                return "Ошибка: на ноль делить нельзя!"
            result = num1 / num2
        else:
            return "Ошибка: неверная операция."

        return f"Результат: {result}"

    except ValueError:
        return "Ошибка: вводите только числа."

# Запуск программы
print(calculator())