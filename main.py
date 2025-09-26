while True:
    a = input("Введите первое число (или 'exit' для выхода): ")
    if a.lower() == "exit":
        print("Калькулятор завершил работу.")
        break

    b = input("Введите второе число (или 'exit' для выхода): ")
    if b.lower() == "exit":
        print("Калькулятор завершил работу.")
        break

    op = input("Введите операцию (+, -, *, /), или 'exit' для выхода: ")
    if op.lower() == "exit":
        print("Калькулятор завершил работу.")
        break

    try:
        a = float(a)
        b = float(b)

        if op == "+":
            print("Результат:", a + b)
        elif op == "-":
            print("Результат:", a - b)
        elif op == "*":
            print("Результат:", a * b)
        elif op == "/":
            if b == 0:
                print("Ошибка: деление на ноль!")
            else:
                print("Результат:", a / b)
        else:
            print("Ошибка: допустимы только '+', '-', '*' и '/'.")
    except ValueError:
        print("Ошибка: нужно вводить числа!")
