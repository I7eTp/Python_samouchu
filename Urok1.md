Типы переменных

None - отсутствие данных

int - Целое число

x = input(’Вод ‘)     При вводе с клавиатуре значение Х будет строка.

r = x + 5                при складывание строки и чесла  будет ошибка.

r = int(x) + 5         Для этого нужно Х присвоить переменную целого числа int(x)

_________________________________________________________________________________________________

float -Число с плавающей точкой

x = input(’Вод ‘)     При вводе с клавиатуре значение Х будет строка.

r = x + 5                при складывание строки и числа  будет ошибка.

r = float(x) + 5      Для этого нужно Х присвоить переменную с плавающей точкой float(x)

___________________________________________________________________________________________________

Значение int и float могут конвертировать значение 

если значение float число переводит в число с плавающей точкой 

пример:  float(5)  float = 5.0

А int число с точкой округляет отбрасывая всё что после точки. 

пример: int(5.8) int = 5

____________________________________________________________________________

str - Строка содержит текст буквы цыфры знаки. 

```python
x = float(input ('Введите число '))
y = float(input ('Введите число '))
r = x + y
print('Результат ' + str(r))

пример ответа:
Введите число 34 ввели одно целое 
Введите число 12.4 ввели с плавающей запятой 
Результат 46.4  в строке ответа используем текст(print('Результат ' + str(r)) и присваеваем числовому значению в текстовое str(r). 
Если мы это не сделаем будет ошибка.

print('Результат ' + r)
TypeError: can only concatenate str (not "float") to str   
```

____________________________________________________________________________________________________

complex - комплексное число 

list - 

tuple - 

set - 

dict - 

bool - Булевое значение данных

# Урок № 2 __Самообразование изучение Python__ 
__Условные операторы и операторы сравнения__
**Часть1**

__True - Истина,  Правда__ 
__False -Лож, Не правда__

```python
if True:
    print('if')
elif True:
    print('elif')
else:
    print('else')
Если в условном операторе будет истина (True). То код первого опиратора сработает 
  print('if'). 
выдет ответ if
Все остальные нет.

Если оператором сравнения будет лож(False)
if False:
    print('if') То код первого опиратора не сработает print('if'). 
elif True:
    print('elif') Cработает код второго оператора print('elif'). 
else:
    print('else')

И третий вариант если обо сравнения лож сработает третий код оператора print('else')
if False:
    print('if')
elif False:
    print('elif')
else:
    print('else') сработает третий код оператора print('else')

Пример решения задачи:
x = -3
if x == 0:
    print('равен 0')
elif x > 0:
    print('больше 0')
else:
    print('меньше 0')
================= RESTART: =================
меньше 0

x = 0
if x == 0:
    x = x - 2  # (x += 1 сокрашение написания)

print(5/x)
```

__Условные операторы и операторы сравнения__
**Часть2**

_________________________________________________________________________________________________________

not - меняет булевое значение на противоположное  

пример:  

if not x == 0: Если Х равен True.  То ответ будет False

_________________________________________________________________________________________________________

or - Достаточно что бы хоть с одной стороны было True 

пример:

elif type(x) == type(5) or type(x) == type(5.5):

__________________________________________________________________________________________________________

and - Условие выполниться если при сравнение значение и с права и слева будут True 

пример:

elif type(x) == type(5) and type(x) == type(5.5):

__________________________________________________________________________________________________________
```python


x = 5   # Х = целовому данные, 
        # а если будет (x = 'a') строка выдаст ответ: 
        # X не допустимый тип данных
100.0 

if x == 5.5:
    x = 1
    print('Х был равный Нулю')

elif type(x) == type(5) or type(x) == type(5.5):
    print('X допустимое значение')

else:
    print('X не допустимый тип данных')
    x = 1

print(100/x)

ответ:
X допустимое значение
20.0
```
