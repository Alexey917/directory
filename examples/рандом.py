### рандом

import random # Подключаем бибилотеку

x = random.randint(1, 6)       # Случайное число от 1 до 6
x = random.random()            # Случайное число от 0 до 1 дробное

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)      # Случайный выбор из списка

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.suffle(cards)            # Случайное перемешивание списка