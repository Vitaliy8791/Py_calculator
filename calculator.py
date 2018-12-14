my_choise = "start"
while my_choise == "start":
    try:
        def sub(x, y):
            return x - y


        def mul(x, y):
            return x * y


        def add(x, y):
            return x + y


        def del_num(x, y):
            return x / y


        def step(x, y):
            return x ** y


        def choises(chois):
            while chois != "start" and chois != "stop":
                a = """Введите "start". - Для перезапуска калькулятора"""
                b = """Введите "stop". - Для завершения калькулятора"""
                print(a, b, sep="\n")
                chois = input()
            return chois


        def calculator(calc):
            one_num = None
            result = 0
            while result is not None:
                if one_num is None:
                    one_num = float(input('Введите первое число: '))
                oper = input('Введите действие или exit для выхода:  ').lower()
                if oper == "exit":
                    result = None
                    continue
                two_num = float(input('Введите второе число: '))

                if oper in list(calc.keys()):
                    result = calc[oper](one_num, two_num)
                    print("Результат: ({}) {} ({}) = {} ".format(one_num, oper, two_num, result))
                    print("-------------------------------------------")
                    one_num = result
                else:
                    print('Операция ', oper, 'не входит в перечень операций!')

            return oper
        dict_calculator = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': del_num,
            '**': step
        }
        my_choise = choises(calculator(dict_calculator))
    except ZeroDivisionError:
        print("Деление на ноль запрещено!")
    except ValueError as e:
        print("Некорректный ввод!")
        print("Error: ", e)
