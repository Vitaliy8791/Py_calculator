from math import sin


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


def sin_num(x):
    return sin(x)


def choises(chois):
    while chois != "start" and chois != "stop":
        a = """Введите "start". - Для перезапуска калькулятора"""
        b = """Введите "stop". - Для завершения калькулятора"""
        print(a, b, sep="\n")
        chois = input()
    return chois


dict_calculator = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': del_num,
    '**': step
}

calc_fun = {
    'sin': sin_num
}