### str.format() - метод дающий больше возможностей при выводе строки в консоль

animal = "cow"
item = "moon"
name = "Bro"
pi = 3.1415
number = 1000
print("The {} jumped over the {}".format(animal, item))  # "The cow jumped over the moon"
print("The {1} jumped over the {0}".format(animal, item)) # "The moon jumped over the cow"
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # "The cow jumped over the moon"
#пробелы
print("Hello, my name is {:10}. Nice to meet you".format(name)) # "Hello, my name is Bro.           Nice to meet you" 10 пробелов справа
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # "Hello, my name is Bro.           Nice to meet you"  по левому краю  
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # "Hello, my name is           Bro.Nice to meet you" по правому краю
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # "Hello, my name is     Bro.     Nice to meet you" по центру
print("The number pi is {:.2f}".format(pi)) # "The number pi is 3.14" два знака после запятой 
print("The number pi is {:,}".format(number)) # "The number pi is 1, 000" отделит тысячу, миллион и.т.п
print("The number pi is {:b}".format(number)) # "The number pi is 1111101000" бинарное представление
print("The number pi is {:о}".format(number)) # "The number pi is 1750" восьмеричное представление
print("The number pi is {:X}".format(number)) # "The number pi is 3Е8" шестнадцатиричное представление
print("The number pi is {:E}".format(number)) # "The number pi is 1.000000E+03" по нананаучному