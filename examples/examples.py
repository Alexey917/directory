### @staticmethod и @classmethod

@staticmethod
def func(cls):
    something
    
@classmethod
def func():
    something

# методы класса работают исключительно с атрибутами класса, но не могут обращаться к локальным атрибутам класса
Vector.method() # так норм

# внутри класса к ним нужно обращаться через self.method()

# статический метод не имеет доступ к атрибутам класса и атрибутам экземпляра. Он независмый, сервисный, функционирует сам по себе



### Полиморфизм

# Полиморфизм - возможность работы с совершенно разными объектами единым образом

# Т.е есть функция в нескольких классах, которая называется одинаково, и везде делает разные вещи

# Если в каком то классе отсутствует метод, можно создать родительский класс, и в нем создать метод(с тем же названием) и он будет возвращать 
#raise NotImplementedError("В дочерних классах должен быть переопределен метод get_pr()")

# Абстракты - методы, которые обязательно нужно переопределять в дочерних классах, и он не имеет своей собственной реализации. В python мы их всего лишь имитируем

class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочерних классах должен быть переопределен метод get_pr()")

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def get_pr(self):
        return 2*(self.w + self.h)

class Square(Geom):
    def __init__(self, a):
        self.a = a
        
    def get_pr(self):
        return 4*self.a
    
class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.a = b
        self.a = c
        
geom = [Rectangle(1,2), Square(10), Triangle(1,2,3)]
        
for g in geom:
    print(g.get_pr())
    
### dunder методы - магические методы
__str__() - для отображения информации об объекте класса для пользователя(наприме для функций print, str)
__repr__() - для отображения информации об объекте класса в режиме отладки(для разработчиков)

def __repr__(self):
    return f'{....}'

def __str__(self):
    return f'{...}'

__len__() - позволяет применить функцию len к экземпляру класса
__abs__() - позволяет применить функцию abs к экземпляру класса

def __len__(self):
    return len(self.__coords)


__add__() - для операции сложения
__sub__() - для операции вычитания
__mul__() - для операции умножения
__truediv__() - для операции деления
__floordiv__() - для операции целочисленного деления
__mod__() - для операции остаток от делания 

class Clock:
    __DAY = 86400 # число секунд в одном дне
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int): # (seconds, int) - указываем какого типа будет second
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY
        
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0") # добавляет не значащий ноль к цифрам(для формата времени)
    
    def __add__(self, other): # other - это то что будет справа от экземпляра класса
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        return Clock(self.seconds + sc)
    
    def __radd__(self, other): # если объект класса записан справа
        return self + other
    
    def __iadd__(self, other): # для с += 100 не создает новый экземпляр класса, а просто увеличивает на 100
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        self.seconds += sc
        return self
    
c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2   # __add__
c4 += 100      # __iadd__
c5 = 100 + c1  # __radd__

class A:
     def __init__(self, x):
          self.x = x

def __add__(self, other):
     obj = A(self.x)
     obj.x += other.x # other объект класса А к которому мы прибавляем
     return obj

def __str__(self):
     return str(self.x)

# чтобы провернуть такую операцию += нужно:

def __iadd__(self, other):
     self.x += other.x
     return self

obj1 + obj2 # obj2 это other

### методы сравнений

__eq__() - для равенства ==
__ne__() - для равенства !=
__lt__() - для равенства <
__le__() - для равенства <=
__gt__() - для равенства >
__ge__() - для равенства >=

@classmethod
def __verify_data(cls, other):
     if not isinstance(other, (int, Clock)):
          raise TypeError("Операнд справа должен иметь тип int или Clock")
     return other if isinstance(other, int) else other.seconds

def __eq__(self, other):
     sc = self.__verify_data(other)
     return self.seconds == sc

def __lt__(self, other):
     sc = self.__verify_data(other)
     return self.seconds < sc

def __le__(self, other):
     sc = self.__verify_data(other)
     return self.seconds <= sc

eq - сработает и на с1 != с2 в виде not(c1 == c2)
lt - сработает, если нет gt. Если с1 > c2, поменяет операнды местами c1 < c2

Т.е на нужен только один метод eq(или ne), lt(или gt), le(или ge)

### @property - для более гибкой работы с приватными свойствами

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        
    
    '''def get_old(self):
        return self.__old
    
    
    def set_old(self, old):
        self.__old = old'''
        
    @property
    def old(self):        # одно и тоже имя функции!
        return self.__old
    
    @old.setter
    def old(self, old):   # одно и тоже имя функции!
        self.__old = old
        
    @old.deleter
    def old(self):
        del self.__old
        
    # эквивалентно
    # old = property(get_old, set_old) # создаем объект класса property, передавая ему уже существующие геттер и сеттер
        
p = Person('Сергей', 20)
del p.old
p.old = 35              # у property приоритет выше чем у операции присваивания, поэтому сначала выполняться геттеры и сеттеры, а потом присваивание. В противном случае создалось бы новое свойство old со значением 35
print(p.old, p.__dict__)

@property - имеет декораторы: x.setter(), x.getter(), x.deleter() 

__setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
__getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
__getattr__(self, item) - автоматически вызывается при получении не существующего свойства item класса
__delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует он или нет)

1) как только идет обращение к свойству через экземпляр класса срабатывает __getattribute__(self, item)

def __getattribute__(self, item):
    if item == "x":
        raise ValueError("доступ запрещен")
    else:
       return object.__getattribute__(self, item)
   
2) срабатывает всегда, когда происходит присвоение к какому то атрибуту

def __setattr__(self, key, value):
    if key == "z":
        raise AttributeError("недопустимое имя атрибута")
    else:
       return object.__setattr__(self, key, value)
        # self.x = value - будет выполняться рекурсивно
        # self.__dict__[key] = value - так можно
        
3) вызывается всегда, когда идет обращение к несуществующему атрибуту класса

# можно использовать для обхода ошибок

def __getattr__(self, item):
    return False

4) вызывается, когда удаляется определенный атрибут из экземпляра класса

def __delattr__(self, item):
    object.__delattr__(self, item)
    
    
### Структуры данных

# Big O - показывает динамику изменений динамики вычислительной сложности

# О - верхняя граница оценки сложности алгоритма

# медленная сортировка О(n^2) - например вложенный цикл

# О(1) - выполнение одной операции

# О(С) = О(1) - константа С количество операций

# константы отбрасываются

# Алгоритмы с линейной скоростью О(n)
for x in range(n):   O(n)
    print(x)        
                                O(n+m)
    
for y in range(m):   O(m)
    print(y)
    
    
for x in range(n):  
    for y in range(m):          O(n*m)
        print(x, y)

    
# Неважная сложность 

вложенный цикл - О(n^2)
                           O(n^2 + n)
обычный цикл - О(n)  

# n - становится не важен при n -> бесконечности, поэтому можно отбросить

# Если один показатель может принимать значения больше чем в два раза, то значимо, а другое нет

# Логарифмическая сложность:
# Бинарный поиск О(log n)

# Факториальная сложность:
# NP - полные задачи, т.е полный перебор всех вариантов О(n!)
# самый сложный подход в вычислении
# Градация по объему вычислений по возрастанию:
1) О(1)
2) О(log n)
3) О(n)
4) О(n*log n)
5) О(n^2)
6) О(2^n)
7) О(n!)

### статический массив

# 1) все элементы одного типа
# 2) длина массива фиксированное число
# 3) все элементы хранятся в памяти друг за другом(цельная область)

# size = n * k байт

# arr - ссылка на первый элемент массива

# чтение       О(1)
# запись       О(1)
# вставка      О(n)
# удаление     О(n)

### динамический массив

# добавление в конец О(1)
# в середину О(n)

# если добавляем новый элемент(О(n)) в массив(за пределы), то удваиваем массив

# удаление с конца О(1)

# удалить с середины или сначала - сместить в конец и убавить currentLength - O(n)

# динамический массив меняет число своих элементов в процессе работы программы

# динамические массивы реализуются на основе статических и хранятся в непрерывной области памяти. Операции доступа выполняются за О(1)

# элементы списка в python представляют собой ссылки ведущие на объект

# lst.insert - O(n) - вставка не в конец

# объединение списков - О(n + m)

# срезы О(n)


### Односвязанный список - структура данных в которой элементы ссылаются друг на друга в одном направлении. Двусвязанный - в двух направлениях

# на первый элемент ссылается всегда head, на последний tail
# node - новый объект
# добавление O(1)
# добавление в конец аналогично методу push()
# доступ к произвольному элементу О(n)
# При вставке ищем левый и правый элементы от того места куда хотим вставить. Метод аналог insert(). Сложность O(n)
# удаление из промежутка O(n), аналог erase()
# удаление первого элемента O(1)
# удаление последнего элемента O(n), аналог pop()
# Пример смотри в домашней работе №25

                                                   oneLinked    doublyLinked
добавление в конец                - push_back()  |    O(1)   |    O(1)   
добавление в начало               - push_front() |    O(1)   |    O(1)   
удаление с конца                  - pop_back()   |    O(n)   |    O(1)   
удаление с начала                 - pop_front()  |    O(1)   |    O(1)   
вставка элемента                  - insert()     |    O(n)   |    O(n)   
удаление промежуточного элемента  - erase()      |    O(n)   |    O(n)   
доступ к элементу                 - setAt()      |    O(n)   |    O(n) 

### стек
например история посещений одной вкладки браузера
стек не поддерживает переход к произвольному элементу в отличие от очереди LIFO

стек вызова функций:
    def main()
      a = 5
      print('a = ' + str(a))
      b = 4
      
[top]
  |
  V
[print]
[next]
  |
  V
[main]
[next]
  |
  V
 None
 
 top() - возвращает значение верхнего элемента стека O(1)
 push() - добавляет на вершину O(1)
 pop() - удаляет с вершины O(1)
 size() - возврщает число элементов O(1)
 empty() - возвращает True, если стек пустой, и в противном случае False  O(1)
 
 # очередь 
 FIFO(first in, first out)
 вход -> [буфер данных] -> выход
 пример очереди: интернет заказы 
 LIFO(last in, first out)
 очередь, где можно удалять сначало и конца называются deque (double ended queue). реализуется двусвязанным списком
 
 очередь и стек - абстрактные структуры данных, определящие порядок взаимодействия с элементами
 
 ##### циклический сдвиг:
 
 # влево:
 |0|1|2|3|4|
 tmp = A[0]
 циклом перебираем и tmp вставляем в конец |1|2|3|4|0|
 # вправо:
 |0|1|2|3|4|
 tmp = A[n]
 циклом перебираем и tmp вставляем в начало |4|0|1|2|3|
 
 
 ##### Решето Эратосфена:
 
 A[True]*N
 A[0] = A[1] = False
 for k in range(2, N):
     if A[k]:
         for m in range(2*k, N, k):
             A[m] = False
             
for k in range(N):
    print(k, "-", "простое" if A[k] else "составное")
    

### import struct - для работы ч двоичными данными, сетевыми протоколами и т.д.

# возвращает объект байтов, содержащий значения v1, v2, ..., упакованный в соответствии с "format"
packed_data  = struct.pack("format", v1, v2, ...)

struct.calcsize("format") - вычисляем количество байт для хранения последовательности "format"

# При распаковке получаем кортеж(даже если 1 элемент). Распаковка из буфера packed_data в соответствии "format"
original_data = unpack("format", packed_data)

# запишет упакованные байты в записываемый буферный буфер, начиная со смещения позиции
package_into("format", буфер, смещение, v1, v2, ...)

unpack_from - распаковывает из буфера, начиная со смещения позиции. Результат - кортеж

iter_unpack - итеративно распаковать из буфера в соответствии с форматом. Фукция возвращает итератор, который будет считать из буфера куски одинакового размера до тех пор, пока все содержимое не будет использовано. Размер буфера в байтах должен быть кратен размеру, требуемому форматом. Каждая итерация дает кортеж

calcsize - возвращает размер структуры соответсвующий формату строки

в формате если не указать символ, по умолчанию будет использвать @

little-endian - основной порядок байт(от младшего байта к старшему)
big-endian - основной порядок байт(от старшего байта к младшему)

В сетевых протоколах принято использовать big-endian (символ «!» – псевдоним к «>«), а на большинстве современных настольных систем используется little-endian.

Для строк (коды «s» и «p«) надо указывать число байт – длину строки, иначе будет считаться 1 байт

10s – одна 10-символьная строка, а 10c – 10 отдельных символов

Как узнать на Python какой порядок байт в системе:
import sys
sys.byteorder # 'little' 


Распаковка нескольких однотипных структур:

>>> chunks = struct.pack('hh', 10, 20) * 5 

внутри приложения @ (заполнителем будет - 0l), если другое приложение <>! (заполнителем будет - x)

заполнитель(байт набивки) нужен для выравнивания даных. Данные не дополняются до 8-байтовой границы в конце второй строки формата без использования дополнительного заполнения. Код формата с нулевым повторением решает эту проблему

bytearray в python - массив байт. От типа bytes отличается только тем, что является изменяемым.

Создаём байтовую строку:

b'bytes' # b'bytes'
'Байты'.encode('utf-8') # b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'
bytes('bytes', encoding = 'utf-8') # b'bytes'
bytes([50, 100, 76, 72, 41]) # b'2dLH'

 Функция bytes принимает список чисел от 0 до 255 и возвращает байты, получающиеся применением функции chr
 
 chr - Эта функция возвращает строку, представляющую символ Unicode-код которой соответствует числу i переданному в эту функцию. Например, chr(97) возвращает строку 'a' , а chr(8364) - строку '€' . Это обратная функция ord()
 
 Функция encode() в Python используется для кодирования строки с использованием предоставленной кодировки. Эта функция возвращает объект байтов. Если мы не предоставляем кодировку, по умолчанию используется кодировка «utf-8

Функция decode() используется для преобразования байтов в строковый объект.


### pickle

Модуль pickle реализует двоичные протоколы для сериализации и десериализации структуры объекта Python. "Pickling" - это процесс, посредством которого иерархия объектов Python преобразуется в поток байтов, а "unpickling" - обратная операция, посредством которой поток байтов, из двоичного файла или объекта, подобного байту преобразуется обратно в иерархию объектов.

Чтобы сериализовать иерархию объектов, вы просто вызываете функцию pickle.dumps(). Аналогично, для десериализации потока данных вы вызываете функцию pickle.loads(). Если нужно больше контроля за упаковкой и особенно распаковкой данных, то можно создать объект pickle.Pickler() или pickle.Unpickler() соответственно.

Для справки: функции, названия которых оканчиваются на символ 's' (dumps, loads) - работают со строками.

В формах заполняемых пользователем или инпутах не нужно использовать pickle, там безопаснее будет json

pickle.dump('что записывать', 'куда записывать')
pickle.load(file)

JSON расшифровывается как JavaScript Object Notation.

Итак, dump отличается от dumps тем, что dump записывает объект Python в файл JSON/bin, а dumps сериализует объект Python и хранит его в виде строки.

У нас уже есть JSON-файл, который мы записали выше. Прочитаем его и выведем на экран с помощью функции load в Python

С другой стороны, если имеется строка с JSON нотацией, то чтобы преобразовать её в словарь, используется функция loads

Функция

Определение

dump

Записывает Python-объекты в файл JSON

dumps

Сохраняет объект в виде строки с нотацией JSON

load

Прочитывает файл JSON и возвращает его в виде объекта

loads

Преобразует строку с нотацией JSON в объект

### модуль time

Самый простой способ измерить время выполнения программы — использовать модуль time. В основе этого подхода лежит идея о том, что нужно зафиксировать время в момент начала выполнения программы, а затем, когда программа закончит работу, снова зафиксировать время и вычесть из него время начала. Разница между конечным и начальным временем и будет временем выполнения программы.

import time
 
start_time = time.time()  # время начала выполнения
 
# ваш код
 
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")

В этом примере функция time() модуля time возвращает текущее время в секундах с начала эпохи (обычно это 00:00:00 1 января 1970 года).



from datetime import datetime
 
start_time = datetime.now()  # время начала выполнения
 
# ваш код
 
end_time = datetime.now()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")

В этом примере функция datetime.now() возвращает текущее дату и время, а разница между конечным и начальным временем вычисляется как разность между двумя объектами datetime.


### паттерн builder - Отделяет конструирование сложного объекта от его представления, так что в результате одного и того же процесса конструирования могут получаться разные представления.

От абстрактной фабрики отличается тем, что делает акцент на пошаговом конструировании объекта.
Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика возвращает объект немедленно.
Строитель часто используется для создания паттерна компоновщик.

Применяем когда, свойств много и они имеют неоднозначное значение

Паттерны - это не про новые возможности языка. Это скорее способы построения архитектуры, которую можно легко поддерживать и улучшать

Смысл паттерна builder - переместить определение свойств в другой класс

Это помогает если  какого то свойства у объекта не должно быть, а другого должно, то это свойство надо как то пропустить


from abc import ABCMeta

# Результат производства нашей системы
class Phone:
    def __init__(self):
        self.data: str = '' # данные о телефоне
        
        
    def about_phone(self) -> str:
            return self.data
        
    # добавление информации о той или ной стадии производства телефона
    def append_data(self, string: str):
        self.data += string
        
# Интерфейс разработчика телефона        
class IDeveloper(metaclass=ABCMeta):
    def create_display(self):
        pass
    
    def create_box(self):
        pass
    
    def system_install(self):
        pass
    
    def get_phone(self):
        pass
    
# Разработчик телефонов на андройд платформе
class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()
        
    def create_dispaly(self):
        self.__phone.append_data('Произведен дисплей Samsung; ')
        
    def create_box(self):
        self.__phone.append_data('Произведен корпус Samsung; ')
    
    def system_install(self):
        self.__phone.append_data('Установлена система Android; ')
    
    def get_phone(self) -> Phone:
        return self.__phone
    
    
# Разработчик телефонов на iphone платформе
class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()
        
    def create_dispaly(self):
        self.__phone.append_data('Произведен дисплей Iphone; ')
        
    def create_box(self):
        self.__phone.append_data('Произведен корпус Iphone; ')
    
    def system_install(self):
        self.__phone.append_data('Установлена система IOS; ')
    
    def get_phone(self) -> Phone:
        return self.__phone
    
# Для управления разрботчиками
class Director:
    def __init__(self, developer: IDeveloper):
        self.__developer = developer
        
    # назначается текущий разработчик подчиняющийся директору
    def set_developer(self, developer: IDeveloper):
        self.__developer = developer

    # у директора есть возможность смонтировать  и выпустить телефон без установки системы
    def mount_only_phone(self) -> Phone:
        self.__developer.create_box() 
        self.__developer.create_display() 
        return self.__developer.get_phone()
    
    # Смотирвать и выпустить с операционной системой
    def mount_full_phone(self) -> Phone:
        self.__developer.create_box() 
        self.__developer.create_display() 
        self.__developer.system_install()
        return self.__developer.get_phone()
    
if __name__ == '__main__':
    androd_developer: IDeveloper = AndroidDeveloper()
    
    director = Director(androd_developer)
    
    samsung: Phone = derector.mount_full_phone()
    
    print(samsung.about_phone())
    
    iphone_developer: IDeveloper = IphoneDeveloper()
    
    director = Director(iphone_developer)
    
    iphone: Phone = derector.mount_only_phone()
    
    print(iphone.about_phone())
    
    
## Второй вариант builder
class Phone:
	def __init__(self):
		self.os = None
		self.camera = None
		self.battery = None
		self.screen = None

class PhoneBuilder:
	def __init__(self):
		self.phone = Phone()

	def set_os(self, os):
		self.phone.os = os
		return self

	def set_camera(self, camera):
		self.phone.camera = camera
		return self

	def set_battery(self, battery):
		self.phone.battery = battery
		return self

	def set_screen(self, screen):
		self.phone.screen = screen
		return self

	def get_phone(self):
		return self.phone

builder = PhoneBuilder()
iphone = builder.set_os("Android").set_camera("12 MP").set_battery("3500 mAh").set_screen("6.2 inches").get_phone()

### паттерн фабричный метод

Фабричный метод — это порождающий паттерн проектирования, который позволяет подклассам изменять создаваемый объект, в зависимости от контекста. Объединяя сущности в обобщенную абстракцию.

Предоставление дочерним классам интерфейса для создания экземепляров некоторого класса

Делегирование создания объекта наследникам класса

Позволяет сделать код не привязанным к конкретным классам

недостаток - на каждое представление нужно создавать отдельный класс

class IProduct:
    # Абстрактное представление выпуска автомобиля
    def realese(self):
        pass

# Конкретная машина    
class Car(IProduct):
    def realese(self):
        print('Выпущен новый легковой автомобиль')
        

# Конкретный грузовик  
class Truck(IProduct):
    def realese(self):
        print('Выпущен грузовой автомобиль')
 
# Абстрактное представление цеха по производству легковых автомобилей    
class IWorkShop:
    def create(self) -> IProduct:
        pass
    
# Цех по производству легковых автомобилей
class CarWorkShop(IWorkShop):
    def create(self) -> IProduct:
       return Car()
   
# Цех по производству грузовиков 
class TruckWorkShop(IWorkShop):
    def create(self) -> IProduct:
       return Truck()
   
if __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()
    
    creator = TruckWorkShop()
    truck = creator.create()
    
    car.realese()
    truck.realese()
    
## второй пример фабричного метода

class Document(object):
    def show(self):
        raise NotImplementedError()
 
 
class ODFDocument(Document):
    def show(self):
        print 'Open document format'
 
 
class MSOfficeDocument(Document):
    def show(self):
        print 'MS Office document format'
 
 
class Application(object):
    def create_document(self, type_):
        # параметризованный фабричный метод `create_document`
        raise NotImplementedError()
 
 
class MyApplication(Application):
    def create_document(self, type_):
        if type_ == 'odf':
            return ODFDocument()
        elif type_ == 'doc':
            return MSOfficeDocument()
 
 
app = MyApplication()
app.create_document('odf').show()  # Open document format
app.create_document('doc').show() # MS Office document format


# Абстрактная фабрика

Абстрактная фабрика — это порождающий паттерн, который позволяет создавать группы взаимозависимых или 
связанных объектов, не конкретизируя классы этих объектов.

Шаблон используется когда программа не должна зависеть от типов объектов и процесса

Плюсы: изолирует конкретные классы, упрощает замену продуктов, гарантирует сочетание продуктов
Минусы: сложность добавления поддержки новых продуктов

Свое понимание: абстрактная фабрика это абстрактный класс, который будет потом реализован в виде 
какого то класса и внутри него будет абстрактный метод, который будет возвращать объект(ы) 
другого(их) класса(ов), может там быть условие, в зависимости от которого будет возвращаться тот или 
иной объект. А фабричный метод это метод в котором будет возвращаться объект(или несколько объектов) 


Отличия фабричного метода от абстрактной фабрики:
    - Фабричный метод используется только для  создания одного продукта,  но Абстрактная Фабрика предназначена для  создания семейств связанных или зависимых продуктов .
    - Если мы думаем только о  средствах создания продукта  и  клиенте,  который его использует, то ясно, что в Factory Method мы ограничены в использовании  наследования (на основе классов), а в Abstract Factory у нас есть гибкость  композиции  (на основе объектов) для создания конкретные продукты.
    - Фабричный метод — это  просто метод,  а абстрактный Фабрика — это  объект . Цель  методы фабрики класса , имеющее это  не только создавать  объекты, это делает другую работу также,  только метод отвечает  за  создание  объекта. В Абстрактной Фабрике  вся цель  класса —  создать семейство объектов.
    - Поскольку абстрактная фабрика находится на более высоком уровне абстракции, она  часто использует  фабричный метод для создания продуктов на фабриках.

class AbstractFactory(object):
    def create_drink(self):
        raise NotImplementedError()
 
    def create_food(self):
        raise NotImplementedError()
 
class Drink(object):
    def __init__(self, name):
        self._name = name
 
    def __str__(self):
        return self._name
 
    class Food(object):
        def __init__(self, name):
            self._name = name
 
        def __str__(self):
            return self._name
 
class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-cola')
 
    def create_food(self):
        return Food('Hamburger')
 
class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Pepsi')
 
    def create_food(self):
        return Food('Cheeseburger')
 
def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()
 
factory = get_factory(1)
print factory.create_drink() # Pepsi
print factory.create_food() # Cheeseburger

# второй пример Абстрактной фабрики

from abc import ABCMeta, abstractmethod
 
# абстрактное представление выпускаемого заводом двигателя
class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def realese_engine(self):
        pass
    
class JapaneseEngine(IEngine):
    def realese_engine(self):
        print('Японский двигатель')
 
class RussianEngine(IEngine):
    def realese_engine(self):
        print('Российский двигатель')
        
# выпускаемые автомобили на нашем производстве
class ICar(metaclass=ABCMeta):
    @abstractmethod
    def realese_car(self, engine: IEngine):
        pass
    
class JapaneseCar(ICar):
    def realese_car(self, engine: IEngine):
        print('Собрали японский автомобиль')
        engine.realese_engine()


class RussianCar(ICar):
    def realese_car(self, engine: IEngine):
        print('Собрали российский автомобиль')
        engine.realese_engine()
        
# фабрика производства автомобиля и двигателя        
class IFactory(metaclass=ABC):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass
    
    @abstractmethod
    def create_car(self) -> ICar:
        pass
    
    
class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine()
    
    def create_car(self) -> IEngine:
        return JapaneseCar()
    
class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine()
    
    def create_car(self) -> IEngine:
        return RussianCar()
    
if __name__ == '__main__':
    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.crate_car()
    
    j_car.realese_car(j_engine)
    
    r_factory = JapaneseFactory()
    r_engine = r_factory.create_engine()
    r_car = r_factory.crate_car()
    
    r_car.realese_car(j_engine)
    
    
### паттерн декоратор

Паттерн Декоратор(decorator) еще один структурный паттерн, который позовляет наделять объекты новыми 
свойствами и по сути является альтернативой наследованию. В отличии от адаптера не меняет интерфейс!

Применяется когда:
    1. Имеется необходимость не заметно для клиентского кода добавить обязанности существующему объекту
    2. Нет возможности использовать наследование для расширения функциональности объекта
    3. Обязанности накладываемые на объект могут быть с него сняты
    
От себя:
    декоратор это абстрактный класс добавляющий новый абстрактный метод к нашему объекту

## первый вариант декоратора

class Man(object):
    """Человек"""
    def __init__(self, name):
        self._name = name
 
    def say(self):
        print 'Привет! Меня зовут %s!' % self._name
 
 
class Jetpack(object):
    """Реактивный ранец"""
    def __init__(self, man):
        self._man = man
 
    def __getattr__(self, item):
        return getattr(self._man, item)
 
    def fly(self):
        # расширяем функциональность объекта добавляя возможность летать
        print '%s летит на реактивном ранце!' % self._man._name
 
 
man = Man('Александр')
 
man_jetpack = Jetpack(man)
man_jetpack.say()  # Привет! Меня зовут Александр!
man_jetpack.fly()  # Виктор летит на реактивном ранце!

## второй вариант декоратора

from abc import ABC, abstractmethod
 
class IPizzaBase(ABC):
    """Интерфейс декорируемого объекта"""
    @abstractmethod
    def cost(self) -> float:
        pass
    
class PizzaBase(IPizzaBase):
    """Класс декорируемого объекта"""
    def __init__(self, cost):
        self.__cost = cost
        
    def cost(self) -> float:
        return self.__cost
    
class IDecorator(PizzaBase):
    """Интерфейс декоратора"""
    def name(self) -> str:
        pass
    
class PizzaMargarita(IDecorator):
    """На основе PizzaBase получаем пиццу Маргарита"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Маргарита"
        
    def cost(self) -> float:
        return self.__cost + self.__wrapped.cost()
    
    def name(self) -> str:
        return self.__name
    
    class PizzaSalami(IDecorator):
    """На основе PizzaBase получаем пиццу Салями"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Салями"
        
    def cost(self) -> float:
        return (self.__cost + self.__wrapped.cost())*2
    
    def name(self) -> str:
        return self.__name
    
    
if name == '__main__':
    def print_pizza(pizza: IDecorator) -> None:
        print(f"Стоимость пиццы '{pizza.name()}' = {pizza.cost()}")
    
    pizza_margarita = PizzaMargarita(PizzaBase(100), 100)
    print(f"Стоимость основы пиццы = {pizza_base.cost()}")
    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)
    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)
    
    
### паттерн прототип

Позволяет копировать объекты, не обращая внимание на их реализацию

Когда применять:
    1. система не должна зависеть от классов конкретных объектов
    2. когда нужно избежать использования иерархий классов или фабрик, а также параллельных иерархий классов
    3. необходимо избежать множество производных классво, которые отличаются друг от друга только начальными значениями их атрибутов
    
Достоинства:
    ускоряет процесс создания объектов
Недостатки:
    сложно осуществить процесс клонирования составных объектов
    
copy.deepcopy() - выполняет рекурсивную копию всех атрибутов объекта
copy.copy() - поверхностное копирование(любой объект копируется как ссылка, сами данные не копируются)
return type(self) - возвращает новый объект с копией своего состояния

Пример:
    from abc import ABC, abstractmethod
from typing import List
import copy
from creational.builder_with_director import (PizzaSauceType,
                                              PizzaBase,
                                              PizzaDoughDepth,
                                              PizzaDoughType,
                                              PizzaTopLevelType)


class IPrototype(ABC):
    @abstractmethod
    def clone(self): pass


"""
Класс компонуемого продукта
"""
class Pizza(IPrototype):
    def __init__(self,
                 name,
                 dough: PizzaBase = PizzaBase(PizzaDoughDepth.THICK,
                                              PizzaDoughType.WHEAT),
                 sauce: PizzaSauceType = PizzaSauceType.TOMATO,
                 topping: List[PizzaTopLevelType] = None,
                 cooking_time: int = 10
                 ):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cooking_time = cooking_time  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping] if self.topping is not None else 'None'} \n" \
                    f"cooking time: {self.cooking_time} minutes\n" \
                    f"-----------------------------------------"

        return info

    def clone(self):
        topping = self.topping.copy() if self.topping is not None else None
        return type(self)(
            self.name,
            self.dough,
            self.sauce,
            topping,
            self.cooking_time
        )


if __name__ == "__main__":
    pizza = Pizza("Margarita", topping=[PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.BACON])

    print(pizza)
    new_pizza = pizza.clone()  # клонируем объект
    new_pizza.name = "New_Margarita"
    print(new_pizza)
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.name = "Salami"
    salami_pizza.sauce = PizzaSauceType.BARBEQUE
    salami_pizza.topping.append(PizzaTopLevelType.SALAMI)
    print(salami_pizza)


### паттерн команда

Это поведенческий паттерн проектирования, который позволяет разделить например интерфейс и
бизнес-логику, используя класс, который делегирует бизнес-логике действие, 
запрашиваемое отправителем команды. Паттерн Команда по сути устанавливает одностороннюю 
связь от заказчика к исполнителю.Паттерн Команда (как впрочем и другие паттерны 
проектирования отношений между отправителем и получателем запросов) ведет к появлению 
дополнительных классов и усложнению кода.


Используется когда:
1. Необходимо осущствить параметризацию объектов выполняемым действием
2. Запросы должны организовываться в очередь или выполняться по расписанию
3. Важно иметь возможность поддерживать отмену операций или протоколирование изменений

Достоинства:
1. Легко организует операции отмены, повторения и отложенный запуск
2. Позволяет собирать сложные команды из простых

Недостатки:
1. Вводится огромное количество дополнительных классов

## вариант 1:

class Light(object):
    def turn_on(self):
        print 'Включить свет'
 
    def turn_off(self):
        print 'Выключить свет'
 
 
class CommandBase(object):
    def execute(self):
        raise NotImplementedError()
 
 
class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light
 
 
class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()
 
 
class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()
 
 
class Switch(object):
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
 
    def on(self):
        self.on_cmd.execute()
 
    def off(self):
        self.off_cmd.execute()
 
 
light = Light()
switch = Switch(on_cmd=TurnOnLightCommand(light),
                off_cmd=TurnOffLightCommand(light))
switch.on()  # Включить свет
switch.off() # Выключить свет


### паттерн адаптер

Адаптер — это один из структурных паттернов, из названия которого исходит его и назначения. 
По сути это типичный переходник для разных интерфейсов или данных.
1. Адаптер имеет интерфейс, который совместим с одним из объектов.
2. Поэтому этот объект может свободно вызывать методы адаптера.
3. Адаптер получает эти вызовы и перенаправляет их второму объекту, но уже в том формате и 
последовательности, которые понятны второму объекту.

Нужен для преобразования интерфейса одного класса в другой

Используется когда:
1. Интерфейс существующего класса, не соответствует потребностям
2. Необходимо использовать уже существующие производные классы, в которых отсутствует некоторая
общая функциональность, которую нельзя реализовать путем расширения их базового класса

Достоинства:
1. Отделить и скрыть от клиентского кода подробности преобразования различных интерфейсов
2. Позволяет заменить некоторые операции адаптируемого класса

Недостатки:
1. За счет добавляемых классов может усложниться код программы

## 1 вариант адаптера:

from abc import ABC, abstractmethod


class IOven(ABC):
    """Исходный интерфейс плиты,
    где единица измерения температуры - F"""
    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def set_temperature(self, t: float) -> None:
        pass


class ICelsiusOven(ABC):
    """Интерфейс плиты с которым будем осуществлять
    работу в рамках разрабатываемой системы,
    где единица измерения температуры - C"""
    @abstractmethod
    def get_celsius_temperature(self) -> float:
        pass

    @abstractmethod
    def set_celsius_temperature(self, t: float) -> None:
        pass

    @abstractmethod
    def get_original_temperature(self) -> float:
        pass


class OriginalOven(IOven):
    """Класс кухонной плиты, который будем адаптировать"""
    def __init__(self, t: float):
        assert t >= 32, "Мы тут не холодильник реализуем"
        self.temperature = t

    def set_temperature(self, t: float) -> None:
        assert t >= 32, "Печь которая может морозить? Хм... " \
                        "интересненько"
        self.temperature = t

    def get_temperature(self) -> float:
        return self.temperature


class OvenAdapter(ICelsiusOven):
    """Адаптер, позволяющий работать с плитой, где
     единица измерения температуры фаренгейты в
     градусах цельсия"""
    CELSIUS_TO_FAHRENHEIT: float = 9.0/5.0
    FAHRENHEIT_TO_CELSIUS: float = 5.0/9.0
    FAHRENHEIT_ZERO: float = 32.0

    def __init__(self, original_stove: IOven):
        self.stove = original_stove
        self.temperature = self._init_temperature()

    def get_original_temperature(self) -> float:
        return self.stove.get_temperature()

    def _init_temperature(self) -> float:
        return (OvenAdapter.FAHRENHEIT_TO_CELSIUS *
                (self.stove.get_temperature() -
                 OvenAdapter.FAHRENHEIT_ZERO))

    def get_celsius_temperature(self) -> float:
        return self.temperature

    def set_celsius_temperature(self, t: float) -> None:

        new_temperature_stove = (OvenAdapter.CELSIUS_TO_FAHRENHEIT * t +
                                 OvenAdapter.FAHRENHEIT_ZERO)
        self.stove.set_temperature(new_temperature_stove)
        self.temperature = t

if __name__ == "__main__":
    def print_temperature(stove: ICelsiusOven):
        print(f"Original temperature = {stove.get_original_temperature()}"
              f" F")
        print(f"Celsius temperature = {stove.get_celsius_temperature()}")

    fahrenheit_stove = OriginalOven(32)
    celsius_stove = OvenAdapter(fahrenheit_stove)
    print_temperature(celsius_stove)
    celsius_stove.set_celsius_temperature(180)
    print("----------------")
    print("New temperature")
    print("----------------")
    print_temperature(celsius_stove)

## 2 пример адаптера:

import math
 
 
class Hole(object):
    """
    Абстрактная дырка в вашем коде
    """
    def __init__(self, r):
        # задаем радиус дыры
        self.r = r
 
    def put(self, obj):
        # пытаемся поместить
        try:
            # чтобы влезло, нужно,
            # чтобы радиус дырки позволял
            if self.r >= obj.r:
                print u'Лезет!'
            else:
                print u'Не лезет'
        except AttributeError:
            print (u'Переданный объект не умеет вычислять радиус дырки,'
                   u' в которую он влезет! Напишите Адаптер на python!')
 
 
class Square(object):
    """
    Абстрактный квадратный кол, который позволит
    закрыть абстрактную дырку в коде
    """
    def __init__(self, x, h):
        # зададим параметры дрына
        self.x = x
        self.h = h
 
 
class SquareHoleAdapter(object):
    def __init__(self, sq_obj):
        self.sq_obj = sq_obj
 
    @property
    def r(self):
        # половина диагонали квадрата будет как раз влезать
        # в дырку радиусом с полученное значение
        return math.sqrt(2*(self.sq_obj.x**2))/2
 
 
h1 = Hole(5)
h2 = Hole(2)
s1 = Square(5, 7)
s2 = Square(3, 3)
sa = SquareHoleAdapter(s2)
 
h1.put(s1)
>>> Переданный объект не умеет вычислять радиус дырки, в которую он влезет! 
Напишите Адаптер на python!
 
h1.put(sa)
>>> Лезет!
 
h2.put(sa)
>>> Не лезет


### паттерн прокси

Заместитель (proxy) — еще один структурный паттерн, схожий с фасадом или адаптером, только у 
прокси интерфейс полностью повторяет интерфейс замещающего объекта. 
Используется для отложенных действий над самим объектом, ограничения доступа к объекту, 
логирования и т.д.

Позволяет контролировать доступ к объекту, перехватывая его вызовы и выполняя перечень работ до
или после передачи вызова оригиналу объекта

Используется когда:
1. Необходимо создавать тяжелые объекты "по требованию"(виртуальный Proxy)
2. Контролировать(защищать доступ к исходному объекту(защищающий Proxy))
3. Организация логов запросов к серверному объекту(логирующий Proxy)
4. Локальный запуск сервера(удаленный Proxy)
5. Кэширование объекта

Преимущества:
1. Контроль сервисных объектов незаметным для клиента образом

Недостатаки:
1. Увеличение времени ожидания от сервиса/модуля
2. Усложнение кода

## вариант кода 1:

from functools import partial
 
 
class ImageBase(object):
    """Абстрактное изображение"""
    @classmethod
    def create(cls, width, height):
        """Создает изображение"""
        return cls(width, height)
 
    def draw(self, x, y, color):
        """Рисует точку заданным цветом"""
        raise NotImplementedError()
 
    def fill(self, color):
        """Заливка цветом"""
        raise NotImplementedError()
 
    def save(self, filename):
        """Сохраняет изображение в файл"""
        raise NotImplementedError()
 
 
class Image(ImageBase):
    """Изображение"""
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)
 
    def draw(self, x, y, color):
        print 'Рисуем точку; координаты: (%d, %d); цвет: %s' % (x, y, color)
 
    def fill(self, color):
        print 'Заливка цветом %s' % color
 
    def save(self, filename):
        print 'Сохраняем изображение в файл %s' % filename
 
 
class ImageProxy(ImageBase):
    """
    Заместитель изображения.
    Откладывает выполнение операций над изображением до момента его сохранения.
    """
    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)
        self.operations = []
 
    def draw(self, *args):
        func = partial(self._image.draw, *args)
        self.operations.append(func)
 
    def fill(self, *args):
        func = partial(self._image.fill, *args)
        self.operations.append(func)
 
    def save(self, filename):
        # выполняем все операции над изображением
        map(lambda f: f(), self.operations)
        # сохраняем изображение
        self._image.save(filename)
 
 
img = ImageProxy(200, 200)
img.fill('gray')
img.draw(0, 0, 'green')
img.draw(0, 1, 'green')
img.draw(1, 0, 'green')
img.draw(1, 1, 'green')
img.save('image.png')
 
# Заливка цветом gray
# Рисуем точку; координаты: (0, 0); цвет: green
# Рисуем точку; координаты: (0, 1); цвет: green
# Рисуем точку; координаты: (1, 0); цвет: green
# Рисуем точку; координаты: (1, 1); цвет: green
# Сохраняем изображение в файл image.png

## вариант кода 2:

from abc import ABC, abstractmethod


class PizzaOrderFlyWeight:

    def __init__(self, shared_state):
        self.shared_state = shared_state

    def __repr__(self):
        return str(self.shared_state)


class PizzaOrderContext:

    def __init__(self, unique_state, flyweight: PizzaOrderFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return f"уникальное состояние: {self.unique_state} \n" \
               f"разделяемое состояние: {self.flyweight}"


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> PizzaOrderFlyWeight:

        flyweights = list(filter(lambda x: x.shared_state ==
                                           shared_state, self.flyweights))
        if flyweights:
            return flyweights[0]
        else:
            flyweight = PizzaOrderFlyWeight(shared_state)
            self.flyweights.append(flyweight)
            return flyweight

    @property
    def total(self):
        return len(self.flyweights)


class IOrder(ABC):
    @abstractmethod
    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        pass


class PizzaOrderMaker(IOrder):

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = PizzaOrderContext(unique_state, flyweight)
        self.contexts.append(context)

        return context


class ProxyOrderMaker(IOrder):

    def __init__(self, real_subject: PizzaOrderMaker):
        self.__real_subject = real_subject

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        self.__logging(unique_state, shared_state)
        return self.__real_subject.make_pizza_order(unique_state, shared_state)

    def check_access(self) -> bool:
        print('Проверка готовности Proxy')
        return self.__real_subject is not None

    def __logging(self, unique_state, shared_state) -> None:
        print(f"----Логируемые данные заказа----\n"
              f"уникальное состояние: {unique_state} \n"
              f"разделяемое состояние: {shared_state}")


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    pizza_maker = PizzaOrderMaker(flyweight_factory)
    log_proxy = ProxyOrderMaker(pizza_maker)

    shared_states = [(30, 'Большая пицца'),
                     (25, 'Средняя пицца'),
                     (10, 'Маленькая пицца')]
    unique_states = ['Маргарита', 'Салями', '4 сыра']

    orders = [log_proxy.make_pizza_order(x, y)
              for x in unique_states
              for y in shared_states]
    print("#"*20)
    print("Количество созданных пицц:", len(orders))
    print("Количество разделяемых объектов:", flyweight_factory.total)


# фасад

Фасад — структурный паттерн проектирования, позволяющий дать интерфейс более высокого уровня к сложной системе.
В отличии от адаптера, используется новый интерфейс.
Большой минус в том, что в данной концепции, фасад может стать godlike, связанным со всей системой.
Иногда фасад превращают в синглтон, т.к. обычно нужен всего 1 фасад.

Используется когда:
    1. Необходимо предоставить простой или урезанный интерфейс к сложной подсистеме
    2. Необходимо разложить подсистему на отдельные слои

Достоинства:
    1. Позволяет изолировать клиентов от компонентов подсистемы
    2. Ослабляет связанность между ними
Недостатки:
    1. Может разрастись до некого "Божественного объекта", который привязан ко всем классам программы

Своими словами:
    Фасад - собирает в себе реализация других классов. Экземепляры класса  фасад становятся объектами других классов, а методы фасада реализуют методы этих классов

## вариант кода 1:

from abc import ABC, abstractmethod
from enum import Enum

###################Menu and IClient########################
class MenuType(Enum):
    """Тип меню"""
    VEGAN = 1
    NOT_VEGAN = 2
    MIXED = 3


class IMenu(ABC):
    """
    Базовый класс, задающий
    интерфейс создаваемых меню
    """
    @abstractmethod
    def get_name(self):
        pass


class VeganMenu(IMenu):
    def get_name(self):
        return "Вегетарианское меню"


class NotVeganMenu(IMenu):
    def get_name(self):
        return "Не вегетарианское меню"


class MixedMenu(IMenu):
    def get_name(self):
        return "Смешанное меню"


class IClient(ABC):
    """
    Базовый класс, задающий
    интерфейс клиентов пиццерии
    """
    @abstractmethod
    def request_menu(self, menu: IMenu):
        ...

    @abstractmethod
    def form_order(self) -> dict:
        ...

    @abstractmethod
    def eating_food(self):
        ...

    @abstractmethod
    def get_name(self):
        ...


#####################################################


class Kitchen:
    """
    Кухня
    """
    def prepare_food(self):
        print("Заказанная еда готовится!")

    def call_waiter(self):
        print("Отдаем приготовленную еду официанту")


class Waiter:
    """
    Официант
    """
    def take_order(self, client: IClient):
        print(f"Официант принял заказ клиента {client.get_name()}")

    def send_to_kitchen(self, kitchen: Kitchen):
        print("Официант отнес заказ на кухню")

    def serve_client(self, client: IClient):
        print(f"Блюда готовы, несем клиенту c именем {client.get_name()}!")


class PizzeriaFacade:
    """
    Пиццерия на основе паттерна 'Фасад'
    """
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {MenuType.VEGAN: VeganMenu,
                     MenuType.NOT_VEGAN: NotVeganMenu,
                     MenuType.MIXED: MixedMenu}

    def get_menu(self, type_menu: MenuType) -> IMenu:
        return self.menu[type_menu]()

    def take_order(self, client: IClient):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()


class Client(IClient):
    """
    Класс клиента пиццерии
    """
    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu: IMenu):
        print(f"Клиент {self.name} ознакамливается с '{menu.get_name()}'")

    def form_order(self) -> dict:
        print(f"Клиент {self.name} делает заказ")
        return {}

    def eating_food(self):
        print(f"Клиент {self.name} приступает к трапезе")

    def get_name(self):
        return self.name


if __name__ == "__main__":
    pizzeria = PizzeriaFacade()
    client1 = Client("Иван")
    client2 = Client("Александр")
    client1.request_menu(pizzeria.get_menu(MenuType.MIXED))
    pizzeria.take_order(client1)
    client2.request_menu(pizzeria.get_menu(MenuType.VEGAN))
    pizzeria.take_order(client2)
    client1.eating_food()
    client2.eating_food()

# посредник(Mediator)

Поведенческий паттерн проектирования позволяет разлепить связи между классами и берет на себя функцию связывания. Классы будут общаться через класс-посредник.

Используется когда:
    1. Когда классы имеют множество хаотичных связей между собой
    2. Нет возможности повторно использовать класс из-за зависимости множества других классов от него
    3. Необходимо конфигурировать и распределять поведение между классами, без прохождения множества производных классов

Достоинства:
    1. Позволяет централизировать управление и снизить число производных классов
    2. Упрощает взаимодействие между компонентами и устраняет зависимости между ними
Недостатки:
    1. Может сильно усложнить код

Своими словами:
    Посредник - распределяет действия, задачи между объектами класса

## вариант кода 1:

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from random import choice


class OrderType(Enum):
    """Типы возможных заказов"""
    FOOD = 1
    BINGE = 2


class Order:
    """Класс заказа"""
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ под #{self.id} ({self.type.name})"


class Event(Enum):
    """Типы событий обработки заказов"""
    GET_ORDER = 1
    FINISH_ORDER = 2


class WorkerType(Enum):
    """Типы работников пиццерии"""
    WAITER = 1
    CHIEF = 2
    BARMAN = 3


class IMediator(ABC):
    """Интерфейс посредника"""

    @abstractmethod
    def notify(self, worker: Worker, order: Order, event: Event):
        ...

    @abstractmethod
    def add_worker(self, worker: Worker) -> None:
        ...


class Worker(ABC):
    """Абстрактный базовый класс для
    всех сотрудников пиццерии"""

    def __init__(self, name: str, mediator: IMediator):
        self.mediator = mediator
        self.name = name
        self.orders = []
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        ...

    @abstractmethod
    def finish_order(self, order: Order):
        ...

    @abstractmethod
    def type(self) -> WorkerType:
        ...

    def get_orders_id(self) -> List[int]:
        return [it.id for it in self.orders]


class Waiter(Worker):
    """Класс официанта"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Официант {self.name} принял {order}")
        self.mediator.notify(self, order, Event.GET_ORDER)

    def finish_order(self, order: Order):
        print(f"Официант {self.name} отнес {order} клиенту")
        self.orders.remove(order)

    def type(self) -> WorkerType:
        return WorkerType.WAITER


class Barman(Worker):
    """Класс бармена"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Бармен {self.name} принял {order}")

    def finish_order(self, order: Order):
        print(f"Бармен {self.name} выполнил ")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Бармен {self.name} выполняет {order}")
            self.finish_order(order)
        else:
            print(f"Бармен {self.name} грустно разводит руками")

    def type(self) -> WorkerType:
        return WorkerType.BARMAN


class Chief(Worker):
    """Класс шеф-повара"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Шеф {self.name} принял {order}")

    def finish_order(self, order: Order):
        print(f"Шеф {self.name} выполнил {order}")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Шеф {self.name} выполняет {order}")
            self.finish_order(order)
        else:
            print(f"Шеф {self.name} от нечего делать шинкует капусту")

    def type(self) -> WorkerType:
        return WorkerType.CHIEF


class WorkersMediator(IMediator):
    """Посредник обмена сообщениями между
    работниками пиццерии"""

    def __init__(self):
        self.workers = {WorkerType.WAITER: [],
                        WorkerType.BARMAN: [],
                        WorkerType.CHIEF: []}

    def add_worker(self, worker: Worker):
        if worker not in self.workers[worker.type()]:
            self.workers[worker.type()].append(worker)

    def remove_worker(self, worker: Worker):
        if worker in self.workers[worker.type()]:
            self.workers[worker.type()].remove(worker)
        if len(self.workers[worker.type()]) == 0:
            print(f"Внимание работники типа {worker.type().name} "
                  f" отсутствуют!!!")

    def notify(self, worker: Worker, order: Order, event: Event):
        if (event is Event.GET_ORDER and
                worker.type() is WorkerType.WAITER):
            if order.type is OrderType.FOOD:
                chef: Chief = choice(self.workers[WorkerType.CHIEF])
                chef.take_order(order)
            else:
                barman: Barman = choice(self.workers[WorkerType.BARMAN])
                barman.take_order(order)
        elif (event is Event.FINISH_ORDER and
              (worker.type() is WorkerType.BARMAN or
               worker.type() is WorkerType.CHIEF)):
            for waiter in self.workers[WorkerType.WAITER]:
                if order.id in waiter.get_orders_id():
                    waiter.finish_order(order)
                    break
            else:
                print(f"{order} не был доставлен клиенту!!!")
        else:
            raise NotImplemented("Это что ещё за зверь? Оо")


if __name__ == "__main__":
    mediator = WorkersMediator()
    waiter1 = Waiter("Александр", mediator)
    waiter2 = Waiter("Георгий", mediator)
    waiter3 = Waiter("Максим", mediator)
    barmen1 = Barman("Герман", mediator)
    barmen2 = Barman("Алексей", mediator)
    chief = Chief("Станислав", mediator)

    orders = [Order(choice([OrderType.FOOD, OrderType.BINGE]))
              for _ in range(10)]
    for it in orders:
        print("*"*30)
        choice([waiter1, waiter2, waiter3]).take_order(it)
    print("*" * 39)
    print("*"*8 + "Шеф-повар готовит блюда"+8*"*")
    print("*" * 39)
    for it in range(6):
        chief.processing_order()
        print("*" * 30)
    print("*" * 42)
    print("*"*8 + "Бармены смешивают коктейли"+8*"*")
    print("*" * 42)
    for it in range(7):
        choice([barmen1, barmen2]).processing_order()
        print("*" * 30)

## вариант кода 2:

class WindowBase(object):
    def show(self):
        raise NotImplementedError()
 
    def hide(self):
        raise NotImplementedError()
 
 
class MainWindow(WindowBase):
    def show(self):
        print 'Show MainWindow'
 
    def hide(self):
        print 'Hide MainWindow'
 
 
class SettingWindow(WindowBase):
    def show(self):
        print 'Show SettingWindow'
 
    def hide(self):
        print 'Hide SettingWindow'
 
 
class HelpWindow(WindowBase):
    def show(self):
        print 'Show HelpWindow'
 
    def hide(self):
        print 'Hide HelpWindow'
 
 
class WindowMediator(object):
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'setting', 'help'])
 
    def show(self, win):
        for window in self.windows.itervalues():
            if not window is win:
                window.hide()
        win.show()
 
    def set_main(self, win):
        self.windows['main'] = win
 
    def set_setting(self, win):
        self.windows['setting'] = win
 
    def set_help(self, win):
        self.windows['help'] = win
 
 
main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()
 
med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)
 
main_win.show()  # Show MainWindow
 
med.show(setting_win)
# Hide MainWindow
# Hide HelpWindow
# Show SettingWindow
 
med.show(help_win)
# Hide MainWindow
# Hide SettingWindow
# Show HelpWindow


### MVC - model, view, controller

MVC – паттерн проектирования позволяющий эффективно разделить модель данных, представление и обработку действий. В состав MVC входят три паттерна проектирования: наблюдатель, стратегия и компоновщик(хотя это не обязтельно)

view - то что видит пользователь
model - бизнес-логика
controller - осуществляет взаимодействие view и model

view - столовая
model - кухня
controller - касса, где осуществляется заказ и получение еды

# 1 схема:
                    model
 готовка еды    /          \ обработчика
              view      controller
получение еды   \           / заказ
                    user

# 2 схема:

              html      <-     view
                |               |
visitor -> web browser -> controller
                                |
                              model

контроллер - это клей для модели и представления

Чтобы определить, является ли ваше приложение MVC, вам нужно задать себе следующие вопросы:

Если я изменю что-то в представлении, сломаю ли я что-нибудь в модели?
Если я изменю что-то в модели, сломаю ли я что-нибудь в представлении?
Контроллер передает все как в представлении, так и в модели, чтобы им не приходилось взаимодействовать друг с другом?


### Strategy

Поведенческий паттерн, который позволяет определить семейство алгоритмов и вынести их в собственные классы, которые называются — стратегии.

Используется когда:
    1. Имеется множество похожих классов, которые отличаются лишь поведением 
    2. Необходимо скрыть детали реализации алгоритма для других классов
    3. В классе много поведений, реализуемых через большое количество условных ветвлений, где каждая ветка представляет собой разновидность алгоритма

Достоинства:
    1. Предоставляет альтернативу для порождения производных классов
    2. Избавляет от условных операторов при выборе нужного поведения
    3. Инкапсулирует код и данные алгоритмов для остальных классов
Недостатки:
    1. Усложнение кода системы за счет введения дополнительных классов
    2. Клиентскому коду необходимо знать о наличии различных стратегий, а также их различиях

Своими словами:
    Стратегия - в каждом отдельном классе описывается своя стратегия, т.е свой алгоритм в зависимости от ситуации. Может использоваться наследование с переопределением классов

## вариант кода 1:
class ImageDecoder(object):
    @staticmethod
    def decode(filename):
        raise NotImplementedError()
 
 
class PNGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print 'PNG decode'
 
 
class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print 'JPEG decode'
 
 
class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print 'GIF decode'
 
 
class Image(object):
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError('Невозможно декодировать файл %s' % filename)
        byterange = decoder.decode(filename)
        return cls(byterange, filename)
 
    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename
 
 
Image.open('picture.png')  # PNG decode
Image.open('picture.jpg')  # JPEG decode
Image.open('picture.gif')  # GIF decode


## вариант кода 2:

from abc import ABC, abstractmethod
from enum import Enum


class ChiefMood(Enum):
    """Настроение начальника"""
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3


class Strategy(ABC):
    """Интерфейс стратегии"""

    @abstractmethod
    def check_mood_chief(self, mood: ChiefMood) -> bool:
        ...

    @abstractmethod
    def order_processing(self, money: int) -> str:
        ...


class GoodStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        if (mood is ChiefMood.GOOD or
                mood is ChiefMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "Самый лучшый напиток, который возможен!"


class BadStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        if (mood is ChiefMood.BETTER_STAY_AWAY or
                mood is ChiefMood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return "И стакан воды сойдет!"


class NormalStrategy(Strategy):

    def check_mood_chief(self, mood: ChiefMood) -> bool:
        # может у шефа и плохое настроение
        # но клиенты то тут не при чем
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return "Вежливо отказаться от заказа клиента"
        elif money < 10:
            return "Приготовить espresso"
        elif money < 20:
            return "Приготовить капучино"
        elif money < 50:
            return "Приготовить отменный кофе"
        else:
            return "Самый лучшый напиток, который возможен!"


class Barista:
    def __init__(self, strategy: Strategy,
                 chief_mood: ChiefMood):
        self._strategy = strategy
        self._chief_mood = chief_mood
        print(f"Изначальное настроение шефа: {chief_mood.name}")

    def get_chief_mood(self) -> ChiefMood:
        return self._chief_mood

    def set_chief_mood(self, chief_mood: ChiefMood) -> None:
        print(f"Текущее настроение шефа: {chief_mood.name}")
        self._chief_mood = chief_mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f"Клиент отдает за заказ {money} рублей")
        if self._strategy.check_mood_chief(self._chief_mood):
            print(self._strategy.order_processing(money))
        else:
            print("Сделать вид, что не заметил клиента!")


if __name__ == "__main__":
    barista = Barista(NormalStrategy(),
                      ChiefMood.BETTER_STAY_AWAY)
    barista.take_order(20)
    barista.take_order(50)
    barista.set_strategy(BadStrategy())
    barista.take_order(40)
    barista.take_order(200)
    barista.set_strategy(GoodStrategy())
    barista.take_order(40)
    barista.set_chief_mood(ChiefMood.GOOD)
    barista.take_order(0)


### Наблюдатель(observer)

Поведенческий паттерн проектирования, позволяющий подписчику отслеживать изменения издателя.

Используется когда:
    1. Необходимо при модификации одного объекта произвести изменения в других и нет понимания о каком количестве может идти речь
    2. Необходимо в определенных случаях наблюдать за изменениями ряда объектов в разрабатываемой системе

Достоинства:
    1. Позволяет одним объектам на лету подписываться и отписываться от событий другого объекта
    2. Объекты выступающие в качестве подписчиков, не зависят от конкретных классов объектов, генерирующих события и наоборот 
Недостатки:
    1. Оповещение объектов производится в случайном порядке


Своими словами:
    Наблюдатель - пользователь, объект, который может отслеживать изменения или действия издателя
    
## вариант кода 1:

class Subject(object):
    """Субъект"""
    def __init__(self):
        self._data = None
        self._observers = set()
 
    def attach(self, observer):
        # подписаться на оповещение
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)
 
    def detach(self, observer):
        # отписаться от оповещения
        self._observers.remove(observer)
 
    def get_data(self):
        return self._data
 
    def set_data(self, data):
        self._data = data
        self.notify(data)
 
    def notify(self, data):
        # уведомить всех наблюдателей о событии
        for observer in self._observers:
            observer.update(data)
 
 
class ObserverBase(object):
    """Абстрактный наблюдатель"""
    def update(self, data):
        raise NotImplementedError()
 
 
class Observer(ObserverBase):
    """Наблюдатель"""
    def __init__(self, name):
        self._name = name
 
    def update(self, data):
        print '%s: %s' % (self._name, data)
 
 
subject = Subject()
subject.attach(Observer('Наблюдатель 1'))
subject.attach(Observer('Наблюдатель 2'))
subject.set_data('данные для наблюдателя')
# Наблюдатель 2: данные для наблюдателя
# Наблюдатель 1: данные для наблюдателя

## вариант кода 2:

from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderType(Enum):
    """Типы возможных заказов"""
    CAPPUCCINO = 1
    LATTE = 2
    ESPRESSO = 3


class Order:
    """Класс заказа"""
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ под #{self.id} ({self.type.name})"


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...


class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)


class Barista(Subject):
    def __init__(self):
        super().__init__()
        self.__orders: List[Order] = []
        self.__finish_order: List[Order] = []

    def take_order(self, order: Order) -> None:
        print(f"Бариста принял {order}")
        self.__orders.append(order)

    def get_order(self, order_id: int) -> Order:
        order = None
        for it in self.__finish_order:
            if it.id == order_id:
                order = it
                break
        self.__finish_order.remove(order)
        return order

    def processing_order(self):
        if self.__orders:
            order = choice(self.__orders)
            self.__orders.remove(order)
            self.__finish_order.append(order)
            print(f"Бариста выполнил {order}")
            self.notify(order.id)
        else:
            print("Бариста от нечего делать натирает кофемашину")


class Client(Observer):
    def __init__(self, name: str, barista: Barista):
        self.__barista = barista
        self.__name = name
        self.order: Order = None

    def update(self, order_id: int) -> None:
        """принимаем номер текущего выполненного заказа
        и отписываемся от оповещения баристы"""
        if self.order is not None:
            if order_id == self.order.id:
                print(f"Клиент {self.__name} забрал(а) "
                      f"{self.__barista.get_order(order_id)}")
                self.__barista.detach(self)

    def create_order(self) -> None:
        """Метод для формирования заказа
        и подписки на оповещения от баристы
        по выполненному заказу"""
        order_type = choice([OrderType.LATTE,
                             OrderType.CAPPUCCINO,
                             OrderType.ESPRESSO])
        self.order = Order(order_type)
        print(f"Клиент {self.__name} сделал(а) {self.order}")
        self.__barista.attach(self)
        self.__barista.take_order(self.order)


if __name__ == "__main__":
    names = ['Анастасия', 'Анна',
             'Роман', 'Ростислав', 'Руслан']
    barista = Barista()
    clients = [Client(name, barista) for name in names]
    for client in clients:
        print("*"*30)
        client.create_order()
    print("*" * 4 + "Бариста приступает к выполнению заказов" + 4 * "*")
    for _ in range(6):
        print("*"*30)
        barista.processing_order()


### Компоновщик(composite)

Компоновщик — это структурный паттерн, позволяющий представлять группы объектов в виде дерева. В дальнейшем позволяет работать с составным объектом, как с одиночным.

Используется когда:
    1. Объект(модель) системы может быть структурирован в виде дерева
    2. В клиентском коде необходимо единообразно трактовать как составные, так и индивидуальные объекты

Достоинства:
    1. Позволяет определять иерархии классов, в состав которых входят примитивные и составные объекты
    2. Упрощает архитектуру клиента и облегчает добавление новых видов компонетнов
Недостатки:
    1. Создается слишком общий дизайн классов


Своими словами:
    Компоновщик - класс, который собирает из простых объектов сложные, которое в последствии могут использоваться как смостоятельные единицы   

## вариант кода 1:

# Класс представляющий одновременно примитивы и контейнеры
class Graphic(object):
    def draw(self):
        raise NotImplementedError()
 
    def add(self, obj):
        raise NotImplementedError()
 
    def remove(self, obj):
        raise NotImplementedError()
 
    def get_child(self, index):
        raise NotImplementedError()
 
 
class Line(Graphic):
    def draw(self):
        print 'Линия'
 
 
class Rectangle(Graphic):
    def draw(self):
        print 'Прямоугольник'
 
 
class Text(Graphic):
    def draw(self):
        print 'Текст'
 
 
class Picture(Graphic):
    def __init__(self):
        self._children = []
 
    def draw(self):
        print 'Изображение'
        # вызываем отрисовку у вложенных объектов
        for obj in self._children:
            obj.draw()
 
    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self._children:
            self._children.append(obj)
 
    def remove(self, obj):
        index = self._children.index(obj)
        del self._children[index]
 
    def get_child(self, index):
        return self._children[index]
 
 
pic = Picture()
pic.add(Line())
pic.add(Rectangle())
pic.add(Text())
pic.draw()
# Изображение
# Линия
# Прямоугольник
# Текст
 
line = pic.get_child(0)
line.draw() # Линия


## вариант кода 2:

from abc import ABC, abstractmethod


class IProduct(ABC):
    """Интерфейс продуктов
    входящих в пиццу"""
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Product(IProduct):
    """Класс продукта"""
    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundProduct(IProduct):
    """Класс компонуемых продуктов"""
    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product(self, product: IProduct):
        self.products.remove(product)

    def clear(self):
        self.products = []


class Pizza(CompoundProduct):
    """Класс пиццы"""
    def __init__(self, name: str):
        super(Pizza, self).__init__(name)

    def cost(self):
        cost = 0
        for it in self.products:
            cost_it = it.cost()
            print(f"Стоимость '{it.name()}' = {cost_it} тугриков")
            cost += cost_it
        print(f"Стоимость пиццы '{self.name()}' = {cost} тугриков")
        return cost


if __name__ == "__main__":
    dough = CompoundProduct("тесто")
    dough.add_product(Product("мука", 3))
    dough.add_product(Product("яйцо", 2.3))
    dough.add_product(Product("соль", 1))
    dough.add_product(Product("сахар", 2.1))
    sauce = Product("Барбекю", 12.1)
    topping = CompoundProduct("топпинг")
    topping.add_product(Product("Дор блю", 14))
    topping.add_product(Product("Пармезан", 12.3))
    topping.add_product(Product("Моцарелла", 9.54))
    topping.add_product(Product("Маасдам", 7.27))
    pizza = Pizza("4 сыра")
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)
    print(pizza.cost())

### логгирование

- Логи полезны лишь тогда, когда их можно использовать для отслеживания важных ошибок, 
которые нужно исправлять.

- Когда вы работаете над приложением, состоящим из множества модулей — вам стоит 
задуматься о том, чтобы настроить свой логгер для каждого модуля. Установка имени логгера 
в name помогает идентифицировать модуль приложения, в котором имеются проблемы, нуждающиеся 
в решении.

- Всегда включайте в сообщения логов отметки времени, так как они полезны в деле поиска того 
момента, когда произошла ошибка. Единообразно форматируйте сообщения логов, 
придерживаясь одного и того же подхода в разных модулях.

 Для логирования исключений ещё можно воспользоваться конструкцией logging.exception(<message>)

 - нужно залогировать исключение вместе с данными трассировки стека. Чтобы это сделать — 
 можно воспользоваться logging.error(message, exc_info=True). Запустите следующий код и 
 посмотрите на то, как в файл попадают записи с уровнем логирования info, указывающие на то, 
 что код работает так, как ожидается.

import logging

logging.basicConfig(level=logging.DEBUG, filename='msg.log', format='%(levelname)s 
                    %(asctime): %(message)s (Line: %(lineno)d) [%(filename)s]', 
                    datefmt='%d /%m /%Y %I: %M: %S'
                    filemode='w', encoding='utf-8')

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику 
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

py_logger.info(f"Testing the custom logger for module {__name__}...")

x_vals = [2,3,6,4,10]
y_vals = [5,7,12,0,1]

for x_val,y_val in zip(x_vals,y_vals):
    x,y = x_val, y_val
    # вызов test_division
    test_division(x,y)
    py_logger.info(f"Call test_division with args {x} and {y}")


### паттерн итератор

Это один из поведенческих паттернов проектирования, созданный для обхода коллекций 
и упрощения классов хранения данных, 
вынося реализацию (или разные реализации) обхода в другие классы.

Позволяет производить обход составных элементов объекта не раскрывая его внутреннего представления

Используется когда: 
1. Необходимо скрыть детали реализации сложной структуры данных от клиента
2. Необходимо возможноть осуществлять обход одной и той же структуры данных несколькими способами
3. Обход различных структур данных должен осуществляться в рамках единого интерфейса

Достоинства: 
1. Позволяет организовать различные способы и направления обхода структуры данных

Недостатки: 
1. Если достаточно цикла for, его применение не оправдано


От себя:
Итератор класс в котором реализованы методы получение след элемента, проверки наличия след. элемента, вернуть 
элемент по индексу, проверить есть он или нет в структуре, вернуть первый элемент, вернуть последний элемент.
Есть класс агрегат, который использует метод итератор, который в свою очередь возвращает объект класса итератор

##  1 вариант кода 

# coding: utf-8
 
class IteratorBase(object):
    """Базовый класс итератора"""
    def first(self):
        """Возвращает первый элемент коллекции.
        Если элемента не существует возбуждается исключение IndexError."""
        raise NotImplementedError()
 
    def last(self):
        """Возвращает последний элемент коллекции.
        Если элемента не существует возбуждается исключение IndexError."""
        raise NotImplementedError()
 
    def next(self):
        """Возвращает следующий элемент коллекции"""
        raise NotImplementedError()
 
    def prev(self):
        """Возвращает предыдущий элемент коллекции"""
        raise NotImplementedError()
 
    def current_item(self):
        """Возвращает текущий элемент коллекции"""
        raise NotImplementedError()
 
    def is_done(self, index):
        """Возвращает истину если элемент с указанным индексом существует, иначе ложь"""
        raise NotImplementedError()
 
    def get_item(self, index):
        """Возвращает элемент коллекции с указанным индексом, иначе выбрасывает исключение IndexError"""
        raise NotImplementedError()
 
 
class Iterator(IteratorBase):
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0
 
    def first(self):
        return self._list[0]
 
    def last(self):
        return self._list[-1]
 
    def current_item(self):
        return self._list[self._current]
 
    def is_done(self, index):
        last_index = len(self._list) - 1
        return 0 <= index <= last_index
 
    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self.current_item()
 
    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._list) - 1
        return self.current_item()
 
    def get_item(self, index):
        if not self.is_done(index):
            raise IndexError('Нет элемента с индексом: %d' % index)
        return self._list[index]
 
 
it = Iterator(['one', 'two', 'three', 'four', 'five'])
print [it.prev() for i in range(5)]  # ['five', 'four', 'three', 'two', 'one']
print [it.next() for i in range(5)] # ['two', 'three', 'four', 'five', 'one']


## 2 вариант кода

from abc import ABC, abstractmethod
from typing import List


class PizzaItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кусочек пиццы под номером: {self.number}"


class Iterator(ABC):
    @abstractmethod
    def next(self) -> PizzaItem:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem]):
        self._pizza = pizza
        self._index = 0

    def next(self) -> PizzaItem:
        pizza_item = self._pizza[self._index]
        self._index += 1
        return pizza_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._pizza) else True


class PizzaAggregate:
    def __init__(self, amount_slices: int = 10):
        self.slices = [PizzaItem(it+1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали "
              f"на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self.slices)

    def iterator(self) -> Iterator:
        return PizzaSliceIterator(self.slices)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    iterator = pizza.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
    print("*"*20)
    iterator = pizza.iterator()
    iterator.next()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))

## 3 вариант кода

from typing import List
from collections.abc import Iterable, Iterator


class PizzaItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кусочек пиццы под номером: {self.number}"


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem],
                 reverse: bool = False):
        self._pizza = pizza
        self._index: int = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self) -> PizzaItem:
        try:
            pizza_item = self._pizza[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return pizza_item


class PizzaAggregate(Iterable):
    def __init__(self, amount_slices: int = 10):
        self._slices = [PizzaItem(it+1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали "
              f"на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self._slices)

    def __iter__(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices)

    def get_reverse_iterator(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices, True)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    for item in pizza:
        print("Это " + str(item))
    print("*" * 8 + "Обход в обратную сторону" + "*"*8)
    iterator = pizza.get_reverse_iterator()
    for item in iterator:
        print("Это " + str(item))


### unittest

- создаем папку tests, в ней name_test.py

import unittest


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12) # первый аргумет может быть функцией, второй это ожидаемый ответ

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()

В данном примере показан общий шаблон для большинства тестов - здесь и наследование от TestCase, здесь и два простых теста, а также перегрузка встроенных в TestCase методов:

Метод def setUp(self) вызывается ПЕРЕД каждым тестом.
Метод def tearDown(self) вызывается ПОСЛЕ каждого теста

- убедитесь что тесты могут упасть
- положительные тесты(самое основное указать)
- тесты, которые проверяют если что то идет не так

def test_no_signs(self):
    # пытаемся убедиться что исключение работает
    with self.assertRaises(ValueError) as e:
        действие
    self.assertEqual('str', e.exception.args[0])

Как обьединить все тесты:
-выбираем Edit Configuration
-нажиаем +
-ищем python tests
-Unittests
-Custom
-в Additional Arguments пишем discover -s tests -p '*_test.py'

coverage - показывает насколько все протестировано в программе(посмотреть что еще не проверено)

Рекомендации к написанию тестов:

При написании тестов следует исходить из следующих принципов:

Работа теста не должна зависеть от результатов работы других тестов.
Тест должен использовать данные, специально для него подготовленные, и никакие другие.
Тест не должен требовать ввода от пользователя
Тесты не должны перекрывать друг друга (не надо писать одинаковые тесты 20 раз). Можно писать частично перекрывающие тесты.
Нашел баг -> напиши тест
Тесты надо поддерживать в рабочем состоянии
Модульные тесты не должны проверять производительность сущности (класса, функции)
Тесты должны проверять не только то, что сущность работает корректно на корректных данных, но и то что ведет себя адекватно при некорректных данных.
Тесты надо запускать регулярно

## второй пример теста

import unittest


class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        """
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.assertTrue(True)

    def testFailUnless(self):
        """
        Устаревшее название для assertTrue()
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.failUnless(True)

    def testFailIf(self):
        """
        Устаревшая функция, теперь называется assertFalse()
        :return:
        """
        self.failIf(False)

    def testAssertFalse(self):
        """
        Если значение аргумент != False, то кидает ошибку
        :return:
        """
        self.assertFalse(False)

    def testEqual(self):
        """
        Проверка равенства двух аргументов
        :return:
        """
        self.failUnlessEqual(1, 3 - 2)

    def testNotEqual(self):
        """
        Проверка НЕ равенства двух аргументов
        :return:
        """
        self.failIfEqual(2, 3 - 2)

    def testEqualFail(self):
        """
        Ругается если значение аргументов равно
        :return:
        """
        self.failIfEqual(1, 2)

    def testNotEqualFail(self):
        """
        Ругается если значение аргументов не равно
        :return:
        """
        self.failUnlessEqual(2, 3 - 1)

    def testNotAlmostEqual(self):
        """
        Старое название функции.
        Теперь называется assertNotAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения равны
        :return:
        """
        self.failIfAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        """
        Старое название функции
        Теперь называется assertAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения не равны
        :return:
        """
        self.failUnlessAlmostEqual(1.1, 3.3 - 2.0, places=0)


if __name__ == '__main__':
    unittest.main()


### walrus operator

Моржовый (walrus) оператор, появившийся в Python 3.8, дает возможность решить сразу две задачи: 
присвоить значение переменной и вернуть это значение, поэтому порой можно написать код короче и сделать 
его более читаемым, и он может быть даже более эффективным с точки зрения вычислений.

Добавленный в Python 3.8 моржовый оператор (:=), формально известен как оператор присваивания выражения. 
Он дает возможность присвоить переменные в выражении, включая переменные, которых еще не существует. 
Как было сказано выше, с помощью простого оператора присваивания (=) мы назначили num равным 15 в контексте 
отдельного оператора.

food = list()
while True:
    food = input("What food do you like?: ")
    if food == 'quit':
        break
    food.append(food)

foods = list()
while food := input("What food do you like?: ") != 'quit'
    food.append(food)

От себя добавлю: эффективно его испольовать в циклах и принтах


### duck typing

Утиная типизация (duck typing) — это направление в программировании, где в расчет в первую очередь идет 
на поведение и свойства объекта, а не на его тип. При написании функции должны волноваться только о поведении 
и/или атрибутах ее входных параметров, а не о их конкретных типах.

### присвоение функции переменной

В Python мы можем присвоить функцию переменной. И используя эту переменную, мы можем вызывать функцию столько раз, 
сколько захотим. Тем самым увеличивая возможность повторного использования кода. 
Просто присвойте функцию нужной переменной, но без (), т.е. просто с именем функции. 
Если переменной присвоена функция вместе с скобками (), не будет возвращено значение None.

def hello():
    print('Hello')

print(hello) # адрес(с каждым запуском программы он будет разным)
hi = hello
print(hi) # тот же самый адрес
hi() # выведет Hello

say = print
say("Whoa! I can't believe this works! :O") # выведет Whoa! I can't believe this works! :O


### chaning

car = Car()
car.turn_on().drive().brake() # так можно если методы возвращают self

### множественное наследование

многоуровневое наследование и множественное не одно и тоже

множественное наследование - когда дочерний класс наследуется от нескольких родительских классах

многоуровневое - типо матрешка

При множественном наследовании свойства и методы ищутся сначало в дочернем классе, если их нет идем в родительские, и если в одном родительском классе мы нашли, то что искали, то в друго родительский класс мы уже не зайдем, поэтому в __init__ одного из них нужно поместить super().__init__()

MyClass.__mro__ - список классов, которые обходятся в поисках атрибутов или методов

class Notebook(Goods, MixingLog) 

Goods - в __init__ может иметь параметры, все остальные классы не могут MixingLog, и.т.д.

Также Goods будет первый базовый класс в которм будет осуществляться поиск методов или атрибутов, т.к в списке родителей он первый

При полиморфизме:
    Если хотите вызвать метод второго базового класса MixingLog, то нужно прописать MixingLog.название_метода(obj) - obj это объект дочернего класса
    Или переопределить метод в дчернем классе внутри которого указать MixingLog.название_метода(obj), а затем через объект вызвать переопределнный метод


### функции высшего порядка

Функция называется функцией высшего порядка, если она содержит другие функции в качестве 
параметра или возвращает функцию в качестве вывода, т. е. функции, которые работают с 
другой функцией, известны как функции высшего порядка. Стоит знать, что эта функция более 
высокого порядка применима также для функций и методов, которые принимают функции в 
качестве параметра или возвращают функцию в результате. 

Свойства функций высшего порядка:

Функция является экземпляром типа Object.
Вы можете сохранить функцию в переменной.
Вы можете передать функцию в качестве параметра другой функции.
Вы можете вернуть функцию из функции.
Вы можете хранить их в структурах данных, таких как хеш-таблицы, списки и т. д.

Поскольку функции являются объектами, мы также можем возвращать функцию из другой функции. 
В приведенном ниже примере функция create_adder возвращает функцию сумматора.

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))

### лямбда-функции

Лямбда-функции Python являются анонимными функциями, что означает, что функция не имеет имени. 

Синтаксис: лямбда-аргументы: выражение

Эта функция может иметь любое количество аргументов, но только одно выражение, которое вычисляется и возвращается.
Можно свободно использовать лямбда-функции везде, где требуются функциональные объекты.
Вы должны помнить, что лямбда-функции синтаксически ограничены одним выражением.
Он имеет различные применения в определенных областях программирования, помимо других типов выражений в функциях.

def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

Как мы видим в приведенном выше примере, функция Cube() и функция Lambda_cube() ведут себя одинаково

С лямбда-функцией:
- Поддерживает однострочные операторы иногда, которые возвращают некоторое значение.
- Подходит для выполнения коротких операций/манипуляций с данными.
- Использование лямбда-функции иногда может ухудшить читаемость кода.
Без лямбда-функции:
- Поддерживает любое количество строк внутри функционального блока.
- Хорошо подходит для любых случаев, когда требуется несколько строк кода.
- Мы можем использовать комментарии и описания функций для удобства чтения.

Лямбда-функция Python с пониманием списка:

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

Лямбда-функция Python с if-else:

Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

Лямбда-функции не допускают использования нескольких операторов, однако мы можем создать две лямбда-функции, 
а затем вызвать другую лямбда-функцию в качестве параметра первой функции. Попробуем найти второй максимальный 
элемент с помощью лямбды.Код определяет список подсписков под названием ' . 
Он использует лямбда-функции для сортировки каждого подсписка и поиска второго по величине 
элемента в каждом подсписке. Результатом является список вторых по величине элементов, который затем 
распечатывается. В выходных данных отображается второй по величине элемент из каждого подсписка 
исходного списка.List'

List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)





### sort 

Метод Python list sort() сортирует элементы списка. По умолчанию он сортирует значения по возрастанию, 
но также может сортировать значения по убыванию или по своему усмотрению, используя свои параметры.

alphabets = ['a','e','d','c','b'] 
alphabets.sort() 
print(alphabets) 
  
random_numbers = [2,5,6,1,8,3] 
random_numbers.sort() 
print(random_numbers)

Синтаксис сортировки списка Python ()
List_name.sort(reverse=True/False, key=myFunc)

Параметры:
reverse (необязательно): reverse=True, список будет отсортирован по убыванию. По умолчанию reverse=False
key (необязательно) – функция для указания критериев сортировки.

Возвращает:
ортировка списка Python() не возвращает ничего.

Сложность сортировки списка Python составляет O(nlogn)

Разница между sort() и sorted() заключается в том, что список сортировки в Python изменяет список 
напрямую и не выдает никаких результатов, тогда как sorted() не меняет список и возвращает отсортированный список.

сортировка по ключу:

sortSecond = lambda val: val[1] 
my_list1 = [(1, 2), (3, 3), (1, 1)] 
my_list1.sort(key=sortSecond) 
print(my_list1) 
my_list1.sort(key=sortSecond, reverse=True) 
print(my_list1)

Если работаем с кортежами, то применяем sorted

### map

Функция map() возвращает объект map (который является итератором) результатов после применения 
данной функции к каждому элементу данной итерации (списку, кортежу и т. д.).

Синтаксис функции Python map()
Синтаксис : map(funс, iter)

Параметры:

func: это функция, которой map передает каждый элемент заданной итерации.
iter: это итерируемый объект, который необходимо отобразить.
ПРИМЕЧАНИЕ. Вы можете передать в функцию map() одну или несколько итераций.

Возвращает: возвращает список результатов после применения данной функции к каждому элементу данной итерации 
(списку, кортежу и т. д.).

ПРИМЕЧАНИЕ. Возвращаемое значение из map() (объект map) затем можно передать таким функциям, 
как list() (для создания списка), set() (для создания набора). 

пример: 

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

В этом примере мы используем карту и лямбду для добавления двух списков.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
 
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

В этом примере мы используем функцию map() для изменения строки. Мы можем создать карту из итерации в Python.

l = ['sat', 'bat', 'cat', 'mat']
 
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

Временная сложность : O(n)
Вспомогательная сложность: O(n)


### filter

Метод filter() фильтрует заданную последовательность с помощью функции, которая проверяет 
каждый элемент последовательности на истинность или нет. 

Syntax: filter(function, sequence)

функция: функция, которая проверяет, является ли каждый элемент последовательности истинным или нет.

последовательность: последовательность, которую необходимо фильтровать, это могут быть множества, 
списки, кортежи или контейнеры любых итераторов.

Возвращает: итератор, который уже отфильтрован.

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
 
 
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# using filter function
filtered = filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)

общая временная сложность программы равна O(n).    


### Как замерить сложность алгоритма

from time import perf_counter
# enumerate - если нам в цикле нужны индексы, выполняет меньше байт кода
for index, num in enumerate(list):
    temp = num
start = perf_counter()
index_access() # проверяемая функция
print(f'time {perf_counter() - start:.02f}') # расчет скорости выполнения алгоритма

### Абстрактный класс

- Абстрктный класс нужен чтобы запретить пользователю создавать объект этого класса
- вынуждает пользователя переопределить абстрактные методы в дочерних классах
- абстрактный класс - который содержит один или более абстрактных методов
- абстрактный метод - метод, который имеет объявление, но не имеет реализации

Это шаблон, класс призрак, он не реален, это как идея
нужен для проверки(подстраховки) и баланса

Если забыть переопределить в классе абстрактный метод, будет ошибка

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self): pass


class Car(Vehicle):
    def go(self):
        print(f'something')


### дескрипторы

Дескрипторы — это объекты, которые реализуют один или несколько специальных методов: __get__(), __set__() и __delete__(). Они позволяют контролировать доступ к атрибутам класса и определять дополнительное поведение при их получении, изменении или удалении.

## data decroptor:
# проиритет обращения к дискриптору данных выше, чем к локальным свойствам объекта!

class A:
    def __get__(self, instance, owner):
        return ...

    def __set__(self, instance, value):
        ...
    
    def __del__(self):
        ...

## non-data decroptor: могут только считывать данные
# проиритет обращения к дискриптору не данных такой же как локальным свойствам объекта!
class A:
    def __get__(self, instance, owner):
        return ...



class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом!")

    # owner - ссылка на класс Point3D
    # name - x из этого выражения x = Integer() 
    def __set_name__(self, owner, name):
        self.name = "_" + name

    # owner - ссылка на класс Point3D
    # instance - ссылка на объект класса Point3D
    def __get__(self, instance, owner):
        getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)

class Point3D:

    #дискрипторы
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)  


# многопроцессорность

import multiprocessing


def test():
    while True:
    print(f'{multiprocessing.current_process()} - {time.time()}')
    time.sleep(1)

 time.sleep(10)
pr = multiprocessing.Process(target=test, name='prc-1')
print('Процесс запущен')

print(pr.pid) - # узнать id процесса
pr.terminate() - # аналог команды kill, но более безопасный. Убивает процесс
# здесь многие методы похожи на методы threading

# реализация через класс

class Process(multiprocessing.Process):
    def run(self):
        print('work')


pr = Process()
pr.start()


### Архитектура ПО - набор модулей/компонетнов и связей между этими компонентами

# это все должно работать
Принципы:
    DRY
    KISS
    SOLID
    PATTERNS

Удаление/изменение модуля должно быть простым

Работа в команде:
    строгое описание помогает улучшить качество