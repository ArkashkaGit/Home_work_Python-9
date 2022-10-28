# сумма цыфр целого, положительного числа!
def summa (number):
    if type(number) != int:
        raise TypeError ("incorrect data type")
    elif number < 0:
        raise TypeError ("Вы ввели значение меньше нуля")
    else:
        sum = 0
        while number!=0:
            b = number % 10
            sum += b
            number //= 10
        return sum

