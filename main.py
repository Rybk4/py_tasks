while True:
    try:
        a = input("Введите первое число (или 'exit' для выхода): ")
        if a.lower() == "exit":
            print("Калькулятор завершил работу.")
            break
         
        try:
            a = float(a)
        except ValueError:
            print("Ошибка: первое значение должно быть числом!")
            continue

        b = input("Введите второе число (или 'exit' для выхода): ")
        if b.lower() == "exit":
            print("Калькулятор завершил работу.")
            break
         
        try:
            b = float(b)
        except ValueError:
            print("Ошибка: второе значение должно быть числом!")
            continue

        op = input("Введите операцию (+, -, *, /), или 'exit' для выхода: ")
        if op.lower() == "exit":
            print("Калькулятор завершил работу.")
            break
 
        if op not in ['+', '-', '*', '/']:
            print("Ошибка: допустимы только '+', '-', '*' и '/'.")
            continue
 
        if op == "+":
            result = a + b
            print(f"Результат: {a} + {b} = {result}")
        elif op == "-":
            result = a - b
            print(f"Результат: {a} - {b} = {result}")
        elif op == "*":
            result = a * b
            print(f"Результат: {a} * {b} = {result}")
        elif op == "/":
            if b == 0:
                print("Ошибка: деление на ноль невозможно!")
                continue
            result = a / b
            print(f"Результат: {a} / {b} = {result}")
        
        print("-" * 40)
        
    except KeyboardInterrupt:
        print("\n\nКалькулятор завершил работу.")
        break
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        print("Попробуйте еще раз.")
        print("-" * 40)
