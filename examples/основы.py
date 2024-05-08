str = "World!"  # Строковая переменная
number = 5  # Целочисленная переменная
float = 26.5  # С плавающей точкой переменная
bool = True  # Логическая переменная


input()  # Ввод значения с клавиатуры
value = input()  # Ввод строки клавиатуры
value = int(input())  # Приведение к числу и ввод этого числа клавиатуры
value = float(
    input()
)  # Приведение к числу c плаваюей точкой и ввод этого числа клавиатуры
a = str(number)  # Приведение к строке


print("Hello")  # вывод в консоль
print(str)
print("Hello" + " " + str)
print("Hello" + " " + str(number))
print("Hello\nWorld!")  # перенос
print("Hello\tWorld!")  # пробел


strName = "hello world!"
print(len(strName))  # длина строки
print(strName.find("d"))  # индекс символа строки
print(strName.capitalize())  # Переводить первый символ строки в верхний регистр
print(strName.upper())  # Перевод строки в верхний регистр
print(strName.lower())  # Перевод строки в нижний регистр регистр
print(
    strName.isdigit()
)  # Проверяет является ли строка является числом и возвращает true если да, false если нет
print(strName.count("o"))  # Считает количество символов  "o" в строке
print(
    strName.replace("o", "a")
)  # Заменяет все символы  "o"  на "а" в строке или если второго аргумента нет просто удаляет первый
print(strName * 3)  # трижды выводит строку
print(
    strName.split(",")
)  # разбивает строку на список, отделяя каждый элемент знаком, указанным в скобках


import math  # добавляем библиотеку или файлы, добавление делать в самом начале кода
import time


round(number, count)  # Округляем число number с точностью в count знаков после запятой
math.ceil(number)  # Округляем число number до целого числа вверх
math.floor(number)  # Округляем число number до целого вниз
abs(number)  # Число по модулю
pow(number, stepen)  # Возводит число number в степень stepen
math.sqrt(number)  # Вычисляет квадратный корень
max(number, number2, number3)  # Вычисляет максимальное число
min(number, number2, number3)  # Вычисляет минимальное число


name = "hello world!"
first = name[start:stop:step]  # слайсинг-формирование подстроки(обрезание строки)
name[::-1]  # перевернуть строку задом на перед
slice(start, stop)  # тоже самое что и  first = name[start:stop:step]
