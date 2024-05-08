# функция

def nameFunction(parametr1, parametr2):                   # Объявление функции(количество параметров должно совпадать с количеством аргументов)
    print("Какие-то действия")
    return parametr1 * parametr2                          # возвращает результат работы функции(в данном случае произведение)

nameFunction(3, 5)                                        # Вызов функции с позиционными аргументами
nameFunction(parametr2 = 3, parametr1 = 5)                # Иcпользование ключевых параметров

x = nameFunction(3, 5)                                    # заносим значение функции в переменную

-12//5 # ответ -3 при целочисленном делении округление идет в большую сторону, если одно из значений отрицательное
-12 % 5 # ответ 3 тоже самое, но остаток отделения не может быть отрицательный(такое только в python'е)
# или подругому 5 * 3 = 15, 15 % 12 = 3, еще например -11 % 10 = 9, т.к 10*2=20//11=остаток 9

# асинхронный вызов функций  - когда ожидаем результат их выполнения, параллельно выполняются другие действия

# Проектирование сверху вниз. От верхней функции идем в глубь


### Параметр *args - позволяет принимать любое количество аргументов и это будет кортежем, но чтобы
# изменить один из параметром, нужно кортеж преобразовать во что то другое

def add(*args):
    summ = 0
    # тут преобразуем кортеж в список 
    args = list(args)
    args[0] = 0 
    for i in range args:
        sum += i
    return  sum

print(add(1,2,3,4,5,6))

### Когда у нас много ключевых параметров можно использовать кварки, они позволяют принимать любое количество аргументов
# и это будут словари. Это нужно если мы используем ключевые параметры.
# Если мы хотим вывести какой то параметр, то запишется он так: kwargs['parametr']

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
        
        
hello(title="Mr.", first="Bro", middle="Dude", last="Code")