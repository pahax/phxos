operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
    ** для возведения в степень
    ''')
number_1 = int(input('>>>Введите своё первое число: '))
number_2 = int(input('>>>Введите своё второе число: '))
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
elif operation == '**':
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)
else:
    print('Вы ввели недействительный оператор, пожалуйста, запустите программу еще раз.')