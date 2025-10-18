# # print ('Hello World')
# # print('my name Bobur')
# # print('timur say "hello"')
# # print('Hello World')
# # print ('Hello 1 World')
# # print("Hello World")
# # print('Hello')
# # print("'Привет',")
# # print('Меня зовут Вася')
# # print ('и я умнее всех')
# #
# # izi ='«Моя первая переменная!»'
# # print (izi)
# # win ='«И не последняя!»'
# # print  (win)
# #
# # name = 'Иван'
# # my_color = 'Зелёный'
# # sport = 'Бег'
# # print('Меня зовут')
# # print(name)
# # print('Мой любимый цвет:')
# # print(my_color)
# # print('Мой любимый вид спорта:')
# # print(sport)
# #
# #
# # name = input( 'Введите имя: ')
# # print("Hello " + name )
# # name2  = input('Введите фамилию: ')
# # print("Hello " + name2 + ' ' + name + ' я у тебя за спиной!!!')
# #
# # sur_name = input ('Введите фамилию: ')
# # print('Ваша фамилия - ' + sur_name)
# #
# # name = input('Введите имя: ')
# # print("Hello, " + name )
# #
# #
# # name = input('Введите первое слова: ')
# # name2 = input('Введите второе слова: ')
# # print( name + name2)
# #
# # client = 'Петя'
# # pet = 'кот'
# # print(client + ' и ' + pet)
# #
# #
# # r = 'Red'
# # g = 'Green'
# # b = 'Blue'
# #
# # print(r, b, g, r+g+b, b, g+b)
# #
# # aninal1 = input('first animal: ')
# # animal2  = input('second animal: ')
# # print( aninal1 + ' спит, ' + animal2 + ' идёт')
# #
# # name = input('Введите имя: ')
# # name2  = input('Введите фамилию: ')
# # print( "Вас зовут: ")
# # print( name)
# # print(name2)
# #
# # name = input('Введите имя: ')
# # name2  = input('Введите фамилию: ')
# # city3 = input( 'введите город проживания: ')
# # print('===============================')
# # print( "Вас зовут: " + name + ' ' + name2 )
# # print( 'Вы живете в городе: ' + city3 )
# #
# # first_name = input('Введите имя пользователя: ')
# # print ( 'Утро доброе  ' + first_name)
# # print("К сожалению, у Вас нет доступа к системе.")
# # print("Пожалуйста, обратитесь к системному администратору.")
# #
# # city = input ( 'город вылета: ')
# # city2 = input ( 'город прилёта: ')
# # print ('из ' + city + ' - в - ' + city2 + '.')
#
# # first_name = input('Введите имя пользователя: ')
# # greeting = 'Утро доброе'
# # print(greeting, first_name)
# # intro = "К сожалению, у Вас нет доступа к системе."
# # info = "Пожалуйста, обратитесь к системному администратору."
# # print(intro)
# # print(info)
#
# # a = input('Введите первое слово: ')
# # b = input('Введите второе слово: ')
# # print(a, b)
# # a = b
# # b = a
# # print(a, b)
#
# user = input ( 'your name: ')
# new_file  = input ( 'name file: ')
from bisect import insort_right
from queue import PriorityQueue
from selectors import SelectSelector
from xml.dom.minidom import ProcessingInstruction

# =================================================================
# print(3**5)
# print(8/-4)
# print(10/2+6)

# a=5
# b=4
# c=2
# print('сложение:', a+b+c)
# print('вычитание:', a-b-c)
# print('умножение:', a*b*c)
# print('деление:', a/b/c)
# print('степень:', a**b**c)

# a=8
# b=5
# c=3
# print((a/(b+c)-a)/c)


# bus = 5
# metro = 3
# result = (6+((10 - bus)**2))/(metro + 1) + (132 / (2 + bus))
# print(result)

# a=3
# b=8**2
# c=12
# d=4**3**2
# f=2
# g=18
#
# result =(-a+(b-c)*d) / (f*g)
# print(result)

# a=int(input("введите первое число:"))
# b=int(input("введите второе число:"))
# result = a+b
# print('сумма:', result)

# a=int(input("введите первое число:"))
# b=int(input("введите второе число:"))
# c=int(input("введите третье число:"))
# d=int(input("введите четвертое число:"))
# result = 2*(c+5+((a*b)/(4*b)))*(d-2*((a**3)/30))-10
# print('Ответ:', result)


#
# a = '2'
# b = '5'
# c = '3'
# num =  6 ** int(a) + (7 - int(b)) * int(c)
# print(num)

# apple = 41
# box = apple /3
# boxs = apple // 3
# print('всего ящиков: ', boxs)
# print('остаток яблок: ', apple % boxs)
#
# chislo =int(input("Введите число: "))
# chislo =496
# print('номер дома:',chislo%10)
# print('номер квартиры:', chislo//10)






# # Practica
# a = 8
# b = 10
# c = 12
# d = 18
# res=((-3+a**2)*b-2**3)/(c-2*d)
# print(res)

# a=int(input("Enter a number:"))
# b=int(input("Enter b number:"))
# c=int(input("Enter c number:"))
# d=int(input("Enter d number:"))
# e=a+b
# f=c+d
# g=e/f
# print('summa a+b=', e)
# print('summa c+d=', f)
# print('summa (a+b)/(c+d)=',g)

# number =int(input("Введите число: "))
# bolshe = number + 1
# menshe = number - 1
# print('после числа', number ,'идет число',  bolshe )
# print('до числа', number ,'идет число', menshe )

# storona_a =int(input("Введите длину стороны a: "))
# storona_b =int(input("Введите длину стороны b: "))
# otvet = storona_a*storona_b/2
# print('длина двух катетов в прямоугольном треугольнике равно:', otvet)

# minuta =int(input("укажиете кол-во минут : "))
# chas=minuta//60
# ostatok= minuta%60
# print('в часах это:' ,chas)
# print('остаток минут:', ostatok)


# pervoe = int(input("Введите первое 3х значное число: "))
# vtoroe = int(input("Введите второе 3х значное число: "))
# print( (pervoe%100) + (vtoroe%100))

# chislo =int(input("Введите первое 4х значное число: "))
# chislo = 4567
# pervoe = chislo//1000
# vtoroe = chislo%1000//100
# tretiy = chislo%100//10
# chetvertiy = chislo%10
# print(pervoe)
# print(vtoroe)
# print(tretiy)
# print(chetvertiy)



# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# a = 1 # 5
# b = 2 # 1
# c = 3 # 2
# d = 4 # 3
# e = 5 # 4
# print(a, b, c, d, e)
# a=1+2+3+4+5
# b=a-b-c-d-e
# c=a-b-c-d-e
# d=a-b-c-d-e
# e=a-b-c-d-e
# a=
# print(a, b, c, d, e)
# a=1+2+3+4+5



# a = 6
# b = 2
# c = 0
# if b < a:
#     c = a * b
# print(c)


# money = int(input('введите сумму: '))
# if money >= 40000:
#     money -= 40000
#     print('курс успешно приобритен:')
# print( 'Хорошего дня!')

# son  = 5
# father = 5
# if son  == father :
#     print("Угадал")
# print('Конец игры')
#
# son  = 3
# father = 5
# if son  != father :
#     print("Не угадал")
# print('Конец игры')

# money = int(input('введите сумму: '))
# if money >= 1000:
#     money -= 1000
#     print('курс успешно приобритен:')
# else:
#
#     print('Не хватает денег на счёте:')
# print( 'Хорошего дня!')
# print('ostatok  deneg:', money)

# first_number = 10
# second_number = 20
# sum_number = 40
# if sum_number == second_number + first_number:
#     print('Ответ верный!')
# else:#
#     print('Ответ неверный!')


# son  = 5
# father = 3
# if son  == father :
#     print("Угадал")
# else:
#     print("Не угадал")
# print('Конец игры')

# a = int(input("На улице идёт дождь? 1 если да, 2 если нет:  "))
# if 1 == a:
#     print('Пошёл дождь. Возьмите зонтик!')
# else:
#     print('Дождя нет!')



# a= int(input("Введите количество баллов по русскому языку: "))
# b= int(input("Введите количество баллов по математике: "))
# c= int(input("Введите количество баллов по информатике: "))

# a=90
# b=90
# c=30
# d=a+b+c
# if d >= 270:
#     print('Поздравляю, ты поступил на бюджет!')
# else:
#     print('К сожалению, ты не прошёл на бюджет.')

# 4
# a= int(input("сумма первого товара: "))
# b= int(input("сумма второго товара: "))
# c= int(input("сумма третьего товара: "))
# d=a+b+c
# if d >= 10000:
#     summa=d-(d/100*10)
#     print('Поздравляю, тебе хватит!:' , summa)
# else:
#     print('давай заново')

# 5
# a=int(input("Enter a number"))
# if a>0:
#     print("Вы ввели: ", a, 'ответ', a)
# else:
#     suma = a - a - a
#     print("Вы ввели: ",  a, 'ответ', suma)
# 6
# klient = 3
# vladeles = 4
# summa = 7
# print('Кубик Кости:',  klient)
# print('Кубик владельца:' ,vladeles)
# print('Сумма: ',summa)
# selector = SelectSelector()
# if klient <= vladeles:
#     print('Владелец платит:')
# else:
#     print('Игрок платит:')
# print('Игра окончена')


# 7
# chasi = int(input("Введите отработанные часы: "))
# kredit =int(input('Введите остаток по кредиту: '))
# eda = int(input('Введите траты на еду:'))
# chasi = 80
# kredit = 1000
# eda = 5000
# koshel = kredit + eda
# summa = 200*chasi/(2**3)+chasi
# if summa >= koshel:
#     print('Часов хватает. Можно отдохнуть')
# else:
#     print('Часов не хватает. Придётся работать больше!')


# # 8
# a= int(input("Введите первое число: "))
# b= int(input("Введите второе число: "))
# c= int(input("Введите третье число: "))
# if a>b and a>c:
#     print('первое число большое')
# elif b>a and b>c:
#     print('второе число большое')
# elif c>a and c>b:
#     print('третье число большое')



# 555555

# x = 6
# y = 5
# if x>y:
#     print('X больше Y')
# if x<y:
#     print('X меньше Y')
# if x==y:
#     print('X равен Y')
#
#
# bank = int(input('введите сумму: '))
# if bank >= 75000:
#     bank -= 75000
# if bank <= 5000:
#     bank += 1000
#     print('Сделана скид-ка')
# print('курс успешно приобритен:')
# print('Остаток:', + bank)
# print( 'Хорошего дня!')


# money = int(input('введите деньги на покупку:')
# cheese_price = int(input('введите стоимость сыра:')
# ice_cream_price = int(input('введите стоимость мороженого:')
# money = 100
# cheese_price = 80
# ice_cream_price = 20
# posle_sir = money - cheese_price
# if  money >= cheese_price:
#     print('На сыр денег хватило')
# else:
#     print('Денег не хватило даже на сыр!')
# if posle_sir < ice_cream_price:
#     print('Денег маловато')
# else:
#     print('И на мороженое тоже!»')



# x = 2
# y = 2
# if x>y:
#     print('X больше Y')
# elif x<y:
#     print('X меньше Y')
# else:
#     print('X равен Y')


#
# doxod = int(input('какой у вас доход?:'))
#
# if doxod < 10000:
#     print('налог 13% и составляет: ', + (doxod/100*13))
# elif doxod >= 10000 and doxod <= 50000 :
#     print('налог 20% и составляет: ', + (doxod/100*20))
# else:
#     print('налог 30% и составляет: ', + (doxod/100*30))


# first = 2
# second = 2
# third = 1
# if first == second :
#     print("третье легче")
# elif first == third :
#     print("вторая легче")
# else :
#     print("первая легче")


#
# year = 2022
# number_of_speeds = 23
# if  year >= 2018 and number_of_speeds>= 24:
#     print('велик подойдет')
# else :
#     print ('нету')

#
# scores = 280
# medal = 0
# if  scores >= 280 and medal >=1:
#     print('Поздравляем! Ты поступил!')
# else :
#     print ('К сожалению, ты не прошёл в наш университет.')

#
# temperature = int(input("введите градус температуры: "))
# # temperature = 110
# if  temperature >= 0 and temperature <= 100:
#     print('Температура в пределах нормы!')
# else :
#     print ('Опасность! ')

# level = int(input("введите кол-во опыта: "))
# level = 6300
# if level >= 0  and  level <= 999:
#     print('у вас первый уровень' )
# if level >= 1000 and level <= 2500:
#     print('у вас второй уровень')
# if level >= 2500 and  level <= 5000:
#     print('у вас третий уровень')
# if level >= 5000:
#     print('у вас четвертый уровень')
# print ('вы лучший!')


# ball = 290
# status =11
# if ball >= 290:
#     print('Поздравляем! Ты поступил!')
#     if status <= 10:
#         print('Бонусом вам будет начисляться стипендия.')
#     if status >= 11:
#         print('Но вам не хватило баллов для стипендии.')
# else:
#     print('потом повезет!')
#
#
# Задача 4. Опять двойка

# rating = int(input('Что получил по математике? '))
# if rating <=3:
#  print('Плохо. Марш учиться!')
# if rating <= 5:
#  print('Молодец! Можешь отдохнуть.')

# 6
# m2 = 100
# cena =7
# if (m2 >=100 and cena <=10) or (m2 >=80 and cena <=7):
#     print('квартира подходит')
# else:
#     print('квартира не подходит')


# Задача 7. Почта
# Что нужно сделать
# time = int(input('время получение: '))
# time = 9
# if  time >=0 and time <=7 or time >=14 and time <=15 or time >= 10 and time <= 12 or time >= 18 and time <= 20 or  time >= 22 and time <= 24 :
#     print('No working')
# else:
#     print('working')


# 2
#
# X=int(input('Введите значение X:'))
# if  X>0:
#     print('Y=',X-12 )
# if X==0:
#     print('Y=', 5)
# if X<=0:
#     print('Y=', X**2)


# # 66666666666666666
# 1
# total=0
# number = int(input('Введите число: '))
# while number >=0:
#     total += number
#     print(total)
#     number = int(input('Введите число: '))
#     if number == 0:
#         break
# print(total)
# print(number)

# 2
# number = 7
# total = 0
# while number:
#     total += number
#     print(total)
#     if total == 98:
#         break
# print(total )


# Задача 1. Бегать — это полезно
#
# gradus = 20
# total = 0
# while gradus:
#     total += 20
#     gradus -= 2
#     print('длина', total )
#     if gradus <=15 :
#         break
# print('градус', gradus)
# print('растояние' , total+10 )




    #  Задача 2.
# number = 34566432
# nums_total = 0
# while  number:
#     remaider = number % 10
#     if remaider == 5:
#         print("«Обнаружен раз-рыв» 5")
#         break
#     nums_total += remaider
#     number //=10
# print('сумма цифр:', nums_total)



# Задача 3. Начальная школа
# Авторы учебника по математике для второклассников очень любят всё усложнять. Например, отрицатель-ные числа изучают только в пятом классе,
# а они всё норовят дать задачки на них во втором классе. Нам нуж-на программа, которая будет проверять,
# что в учебнике для второклашек не будет отрицательных чисел.
# Напишите программу, которая считывает числа до тех пор, пока не встретит отрицательное число.
# При по-явлении отрицательного числа программа завершается и показывает количество введенных чисел. Поду-майте, обязательно ли здесь использовать оператор break.

# total = int(input("число "))
# while total:
#     total = int(input("число "))
#     print('длина', total )
#     if total <=0:
#         break
# print('растояние' , total )


# limit = 5000
# balance = 13000
# zero = 0
# win = 500
# expense=0
# while balance > limit:
#     expense = int(input('кидайте кубик:'))
#     if  expense ==3:
#         balance -= balance
#     print('у вас в балансе:', balance)
#     elif :, balance += 500
# print('Вы проиграли всё!:' , zero)
# print('у вас в балансе:', balance )
#
#
#
#
# принятие ставки
# money = 10000
# # cube = 1-6
# cube = 0
# int(input('сделайте ставку: '))
# print('Ставки приняты, ставок больше нет!')
# if cube == 3:
#      No_win = 0
# elif
#     cube <=6:
#      No_win = 1
# print ('На счету:', money)




