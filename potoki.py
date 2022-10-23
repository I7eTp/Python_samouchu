x = 5

if x == 5.5:
    x = 1
    print('Х был равный Нулю')

elif type(x) == type(5) or type(x) == type(5.5):
    print('X допустимое значение')

else:
    print('X не допустимый тип данных')
    x = 1

print(100/x)