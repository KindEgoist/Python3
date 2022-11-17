# Конвертор миль в км
# def convert(mili):
#     return mili * 1.609

# mili = float(input('Введите число миль: '))
# km = convert(mili)
# print(f'{mili} милей = {km} километров')
#---------------------------------------------
#Площадь примоугольника по двум сторанам
# def rectangle_area (a, b):
#     return a * b

# length = int(input('Введите число дилины: '))
# width = int(input('Введите число ширина: '))
# s = rectangle_area(length, width)
# print (f'Площадь прямоугольника = {s}')
#---------------------------------------------
#Чет не чет
# def even_or_not_even(num):
#     if num % 2 == 0:
#         return 'Четное'
#     else:
#         return 'Не чет'
# ever = int(input('Введите число: '))
# result = even_or_not_even(ever)
# print(result)
#-----------------------
# Если n > 20 то вернуть 0. Если n <= 20 то пробежаться от 1 до n, возвести каждое четное число в степерь k и вернуть сумму этих чисел
# def function (n, k):
#     if n > 20:
#         return 0
#     else:
#         sum = 0
#         for i in range(2, n + 1):
#             if i % 2 == 0:
#                 res = i ** k
#                 sum += res
#                 print(f'{i} - {res} - {sum}')
#         return sum

# n = int(input('Введите n: '))
# k = int(input('Введите k: '))
# result = function(n, k)
# print (result)
#-----------------------------
# list = [3, 5, 7, 9]

# print('по индексу к элементу')
# for i in range(len(list)):
#     print(f'{i} = {list[i]}')

# print ('Сразу по элементам списка')
# for i in list:
#     print(i)
#-------------------------------
#Сумма отрицательных элементов(идти только по отрицательным)
# list = [-5, -10, -13, -15, -18]
# list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -13, -15, -18]
# sum = 0
# i = len(list) -1 
# while list[i] < 0 and i >= 0:
#     sum += list[i]
#     i -= 1
# print(sum)

# sum = 0
# for i in range(len(list) - 1, -1, -1): # движение по листу с конца к началу
#     if list[i] > 0:
#         break
#     sum += list[i]
# print(sum)
#-----------------------------------
#     
# list = ["apple", "banana", "computer", "music", "stop", "these", "words", "will", "not", "be", "printed"]

# for i in list:
#     if i == "stop":
#         break
#     print(i)

# for i in range(len(list)):
#     if list[i] == "stop":
#         break
#     print(list[i])

# i = 0
# while list[i] != "stop":
#     print(list[i])
#     i += 1
#---------------------------------
# Словари
# # объявление словаря. Пример: dictionary = {}
# d = {"Alex": 25, "Petr": 37} # Ключ : значение
# print(d) # Вывели весь словарь
# print(len(d)) #Длина словаря = 2( две пары)
# d["Kate"] = 18 # Добавит в конец словаря "Kate" : 18
# print(d)
# print(d["Petr"]) # отбращаемся в словаре по ключу и получаем значение
# d["Kate"] = 24 # изменили значение ключа
# print(d)
# d[10] = 20
# del(d["Alex"]) #удаление
# print(d)
# for k, v in d.items(): #проходим по словарю d.keys() по ключам d.values() по значениеям
#     print(k) # отдельно выводим ключ
#     print(v) #отдельно выводим значение
#     print(f'Ключ = {k} и его значение = {v}')
#------------------------------
# Из строки сделать словарь. Где ключь слово, а значение цифры

# list = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 70, 'fourth', -50]
# dictionary = {}
# key = None # переменная которая не содержит нечего
# for e in list: # идем по элементам списка
#     if type(e) == str: # если элемент строка, то
#         dictionary[e] = [] # этот элемент добавляем в словарь с пустым значением
#         key = e # в временную переменную записываем элемент для дальнейшего обращения
#     else:
#         dictionary[key].append(e) # добавляем значение в ключ 
    
# print(dictionary)
#--------------------------
# Создать словарь где ключи будут слова а их значение сколько раз они поподаются в тесте
# text = 'привет пока как дела привет привет арбуз велосипед стол как слон арбуз да привет'

#Вариант мой
# list = text.split()
# dictionary = {}
# key = None
# for e in list:
#     count = 0
#     dictionary[e] = []
#     key = e
#     for e2 in list:
#         if key == e2:
#             count += 1
#     dictionary[key].append(count)
# print (dictionary)

#Вариант 2
# dictionary = {} # создаем словарь
# for e in text.split(): # бежим по тексту со сплитом
#     if e in dictionary: # 2) если слово текущие есть то
#         dictionary[e] = dictionary[e] + 1 # к этому слову(ключу) добавляем значение +1
#     else:
#         dictionary[e] = 1 # 1)  если такого слова нет в словаре то его создаем в виде ключа с параметром 1
# print(dictionary)

# Вариант 3 через функцию get
# dictionary = {} 
# for e in text.split():
#     dictionary[e] = dictionary.get(e, 0) + 1
# print(dictionary)
#----------------------
# Многомерные списки или многомерные массивы
# Создать многомерный список n на m. Значение все нули

# def create_list (m, n): #создание многомерного списка
#     list = []
#     for i in range(m):
#         temp_list = []
#         for j in range(n):
#             temp_list.append(0)
#         list.append(temp_list)
#     return list

# def print_list (list): # функция печати многомерного списка
#     for s in range(len(list)):
#         for e in range(len(list[s])):
#             print(list[s][e], end= ' ')
#         print()

# m = int(input('M= : '))
# n = int(input('N= : '))
# list = create_list(m, n)
# print_list(list)
#---------------------
#Зеркальное отоброжение двухмерного списка

# def create_list (size):
#     list = []
#     count = 10
#     for i in range(size):
#         temp_list = []
#         for j in range(size):
#             temp_list.append(count)
#             count += 1
#         list.append(temp_list)
#     return list

# def print_list(list):
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             print(list[i][j], end= ' ')
#         print()

# def revers_list(list):
#     for i in range(len(list)):
#         for j in range(len(list) // 2): # // цело численное деление вместо for j in range(int(len(list) / 2))
#             list[i][j], list[i][-1 - j] = list[i][-1 - j], list[i][j]
#     return list


# size = int(input('Размер массива: '))
# list = create_list(size)
# print_list(list)
# print('Реверс массива:')
# list2 = revers_list(list)
# print_list(list2)
#------------------------------------
#Генераторы списков(List comprehension)

# list = [1, 2, 3, 4, 5]

# list2 = []
# for num in list:
#     list2.append(num * 2)
# print(list2)
# # сокращенная версия записи 
# list3 = [num * 2 for num in list]
# print(list3)
# # еще пример
# range = [num * 3 for num in range(1, 6)]
# print(range)
# еще пример

# list = [1, 10, 12, 4, 3, 20, 55]
# list_filter = []
# for num in list:
#     if num < 10:
#         list_filter.append(num)
# print(list_filter)

# list_filter2 = [num for num in list if num < 10]
# print(list_filter2)

# list_filter3 = [num ** 2 for num in list if num < 10]
# print(list_filter3)

# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano']
# list_filter = [i for i in list if len(i) < 6]
# print(list_filter)
#-------------------------------
#Результат: [20, 16, 12, 8, 4]
# от 10 до 2. Идем по интервалу от большого к меньшему, берем только четные числа.
# каждое четное чилос мы умнажаем на 2

# list = [i*2 for i in range(10, 1, -1) if i % 2 == 0]
# print(list)
#---------------------
# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano'] если длина больше 5 добавить точку в конце

# list = ['hello', 'hey', 'goodbay', 'guitar', 'piano']
# list_filter = [i + '.' for i in list if len(i) > 5]
# print (list_filter)
#-------------------------
# Множество SET

# set1 = set() # объявление пустого множества. set = {} было бы объявление словаря а не множества
# print(set1)

# set2 = set([1, 10, 5, 'hello']) # 1 способ создание множества
# print(set2)

# set3 = {20, 16, 'hey', 'goodbay', 'guitar'} # 2 способ создание множества
# print(set3)

# set4 = set()
# set4.add(1) # add() добовляет элемент в множество
# set4.add(2)
# set4.add('hello')
# set4.add(10)
# set4.add(2)
# print(set4) #множество хванится не попорядку(как добавляли) и все значение разные, не должно быть повторяющихся элементов

# for el in set4: #вывод всех элементов по очередно в множестве
#     print(el)

# set5 = set() # из списка перекинули элементы в множества, при этом убрали повторяющиеся элементы
# list1 = [1, 2, 1, 1, 5, 'hey', 'hey', 'world']
# # for el in list1:
# #     set5.add(el)
# # print (set5)

# set5 = set(list1) # другой вариант написанного выше без фор. Передали в виде аргумента и получили результат
# print(set5)
# list1 = list(set5) # в лист в качестве аргумента передаем множество
# print(list1)

# set6 = {'hey', 'world',1, 5, 10}
# print(5 in set6) #True ищет указанное значение с помощью (in) в множестве\словаре\списке и т.д.
# print('hey' in set6) #True
# print(2 in set6) #False
# print(15 not in set6) #True
#--------------------------
# Из списка выделить уникальные элементы и получить их сумму
# list1 = [1, 1, 2, 5, 10, 10, 10]
# sum1 = 0
# set1 = set(list1)
# for el in set1:
#     sum1 += el
# print(sum1)
# print(sum(set(list1)))# решение одной строкой. Используем функцию sum() в нее в виде аргумента помещаем функцию set()
# #у которой в качестве аргумента наш список
#----------------------
#Тру если все элементы из списка содержится в множестве. Фолс если нет хоть одного элементы в списки



# def fine (set1, list1):
#     if len(set1) < len(list1):
#         return False
#     for el in list1:
#         if  el not in set1:
#             return False
#     return True
    
# set1 = set([1, 5, 10, 4, 'helloy'])
# list1 = [1, 4, 10, 'helloy']
# x = fine(set1, list1)
# print (x)
#-----------------------
# Объектно орентированное программирование(ООП).

# class Person: #Классы всегда называются с большой буквы
#     def print_info(self,n):
#         for i in range(n):
#             print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')
#     def get_age(self, current_year):
#         print(f'Age: {current_year - self.year_of_birth}')


# p1 = Person() #создание пустого классы в переменной
# p1.name = 'Elon'
# p1.surname = 'Musk'
# p1.place_of_birth = 'ЮАР'
# p1.year_of_birth = 1971

# p2 = Person() 
# p2.name = 'Sergei'
# p2.surname = 'Korolev'
# p2.place_of_birth = 'Российская Империя'
# p2.year_of_birth = 1907

# p3 = Person() 
# p3.name = 'Albert'
# p3.suname = 'Einstein'
# p3.year_of_birth = 1879
# # cсделана ошибка в suname и не назначели поле p2.place_of_birth

# # print(f'Name: {p1.name}, Surname: {p1.surname}, Place of birth: {p1.place_of_birth}')
# # print(f'Name: {p2.name}, Surname: {p2.surname}, Place of birth: {p2.place_of_birth}')
# p1.print_info(2) #вызов функции print_info где аргумент будет выступать параметр p1 вместо аргумента в self 
# p2.print_info(1)

# #Person.print_info(p1,3) # Обращаемся к классу Person и его функции print_info c аргументом p1. Вместо p1.print_info()
# p1.get_age(2022)
# p2.get_age(2022)

# class Person: 
#     def __init__(self, name, surname, place_of_birth, year_of_birth): # функция конструктора. Вместо повторяющегося кода
#         self.name = name
#         self.surname = surname
#         self.place_of_birth = place_of_birth
#         self.year_of_birth = year_of_birth
#     def print_info(self,n):
#         for i in range(n):
#             print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')
#     def get_age(self, current_year):
#         print(f'Age: {current_year - self.year_of_birth}')


# p1 = Person('Elon', 'Musk', 'ЮАР', 1971)
# p2 = Person('Sergei', 'Korolev', 'Российская Империя', 1907)
# p3 = Person('Albert', 'Einstein', 'Германия', 1879)

# p1.print_info(1)
# p2.print_info(1)
# p3.print_info(1)

# class Circle:
#     PI = 3.14

#     def __init__(self, radius):
#         self.radius = radius
#     def get_perimeter(self):
#         return self.radius * 2 * self.PI
#     def get_area(self):
#         return Circle.PI * self.radius ** 2

# c1 = Circle(3)
# print(c1.get_perimeter())
# print(c1.get_area())
# print()
# c2 = Circle(7)
# print(c2.get_perimeter())
# print(c2.get_area())
#-------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Person created')
#     def say_hello(self):
#         print(f'{self.name} says hello!')

# class Student(Person):
#     def __init__(self, name, age, average_grade):
#         #Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.average_grade = average_grade
#         print('Student created')
#     def study(self):
#         print(f'{self.name} studies')
#     def say_hello(self):
#         super().say_hello()
#         print(f'Student with name {self.name} says hello!')

# class Teacher(Person):
#     def teach(self):
#         print(f'{self.name} teaches')

# # s1 = Student('Mike', 18, 4.5)
# # #t1 = Teacher('Katy', 45)
# # s1.say_hello()
# # #t1.say_hello()
# # s1.study()
# # #t1.teach()

# def introduce(person):
#     print('Now, a person will say hello')
#     person.say_hello()
# people_arr = [Student('Tom', 18, 3.5), Teacher('Katy', 35), Student('Bob', 26, 4.8)]
# for person in people_arr:
#     introduce(person)
#-------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f'Dog name {self.name} is barking')
class Cat(Animal):
    def meow(self):
        print(f'{self.name} says Meow')
class Frog(Animal):
    def eat(self):
        print(f'Frog with {self.name} is eating')

d = Dog('Druzhok', 'Terrier')
c = Cat('Barsik')
f = Frog('Kwakwa')

d.bark()
d.eat()
d.breed

c.meow()
c.eat()
f.eat()

