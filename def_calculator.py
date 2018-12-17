def calculator(calc, calc_fun):
    one_num = None
    result = 0
    try:
        while result is not None:
            if one_num is None:
                one_num = float(input('Введите первое число: '))
            oper = input('Введите действие или exit для выхода:  ').lower()
            if oper in list(calc.keys()):
                two_num = float(input('Введите второе число: '))
                result = calc[oper](one_num, two_num)
                print("Результат: ({}) {} ({}) = {} ".format(one_num, oper, two_num, result))
                print("-------------------------------------------")
            elif oper in list(calc_fun.keys()):
                two_num = float(input('Введите число для вычисления синуса: '))
                result = calc_fun[oper](two_num)
                print("Результат: {} ({}) = {} ".format(oper, two_num, result))
                print("-------------------------------------------")
            else:
                if oper == "exit":
                    result = None
                    continue
                print('Операция ', oper, 'не входит в перечень операций!')
                one_num = result
                continue



    except ZeroDivisionError:
        print("Деление на ноль запрещено!")
    except ValueError as e:
        print("Некорректный ввод!")
        print("Error: ", e)

    return oper
