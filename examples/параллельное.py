import threading 
### Параллельное программирование
# при параллельном программировании различные компоненты являются независимыми или частично независимыми и, следовательно, в одно и то же время выполняются
'''
В: Какая основная идея стоит за совместной обработкой и почему она плодотворна?
Что составляет отличия программирования совместной обработки и последовательное программирование?

О: совместная работа не совсем похожа на параллелизм. Несмотря на то, что имеются случаи, когда процессы выполняются вместе(параллельно), совместная работа также вовлекает общее использование одних и тех же ресурсов. 
(рисунок с дорогой и перекрестком)
Наш предыдущий рисунок иллюстрирует основное отличие между совместностью и параллелизмом: в то время как в верхнем отсеке параллельные действия (в данном случае машин), которые не взаимодействуют друг с другом, могут исполняться в одно и то же время, в нижнем отсеке некоторым задачам приходится ждать завершения прочих чтобы они могли быть исполненными.
Комбинирование параллельности и последовательности будет полезнее последовательности(сокращаю время исполнения программы), но не во всех случаях

В: Может ли всякая программа быть превращена в совместную или параллельную?
О: Нет. Зависит от задачи. Иногда может быть так, что программа будет дольше выполняться, чем при последовательном программировании

В: Что представляют из себя задачи с ошеломительной параллельностью?
О: Неким экстремальным примером являются ошеломительно параллельные программы, которые могут быть разделены на различные параллельные задачи между которыми имеется небольшая зависимость или нет её совсем, или же нет потребности во взаимодействии.

В: Что такое задачи с врождённой последовательностью?
О: Эти задачи не являются независимыми и тем самым не могут быть сделаны параллельными или совместными. Более того, если мы бы попытались реализовать в эти программы совместное применение, это могло бы стоить гораздо большего времени исполнения для воспроизводства тех же самых результатов.

В: Что понимается под ограничением со стороны ввода/ вывода?
О: Пока в программе выполняется ввод/вывод, другие задачи находятся в ожидании. Больше времени тратится на запрос данных, нежели на их обработку.

В: Как совместная обработка в настоящее время применяется в реальном мире?
О: Нейросети, облачные хранилища, запросы в поисковиках, запросы на базу данных. настольные и мобильные приложения, видео игры, веб- и интернет- разработка, ИИ и так далее

В: Что из себя представляет Закон Амдала? Какую проблему Закон Амдала пытается решить?
О: Это оценка улучшения потенциального ускорения времени исполнения некоторой задачи, которое мы можем ожидать от системы при улучшении её ресурсов. С ее помощью можно прикинуть идею или наметить стратегию дальнейшего программирования.

В: Объясните основную формулу Закона Амдала, а также ей компоненты.
О: S = T(1) / T(j) = 1 / (B + (1 - B) / j)
T(1) - время выполения с одним процессором
j - количество процессоров
B - та часть программы, которая строго последовательна

В: Будет ли ускорение увеличиваться бесконечно по мере улучшения ресурсов конкретной системы согласно Закону Амдала?
О: Значения различных ускорений при увеличении ресурсов строго уменьшается, а производительность ускорения ограничивается значением накладных расходов последовательного исполнения своей программы.

В: В чём состоит взаимосвязь между Законом Амдала и законом убывающей отдачи?
О: По мере роста общего числа процессоров, значение эффективности, достигаемое от такого улучшения снижается, а получаемая в результате кривая ускорения спрямляется к горизонтальной.
----------------------------------------------------------
Ускорение задачи возрастает с ростом количества процессоров.
Но добавляя новые процессоры, мы будем получать все меньше и меньше улучшений во времени.
Закон Амдала применяется когда имеется программа совместной обработки со смесью параллельных и последовательных инструкций
'''

threading.activeCount(): #Эта функция возвращает общее число активных в настоящий момент времени объектов потока в данной программе

threading.currentThread(): #Данная функция возвращает общее число объектов потока в данном текущем потоке, управляемых стороной вызова

threading.enumerate(): #Функция возвращает список всех активных в настоящий момент объектов потока в данной программе

run(): #Этот метод исполняется когда инициализируется и запускается некий новый поток

start(): #Данный метод запускает инициализированный вызывающий объекта потока, вызывая соответствующий метод run()

join(): #Такой метод ожидает завершения соответствующего вызывающего объекта потока прежде чем продолжить исполнение оставшейся части программы

isAlive(): #Данный метод возвращает Булево значение, указываюшее исполняется ли в данный момент вызывающий объект потока

getName(): #Этот метод возвращает собственно название данного вызывающего объекта потока

setName(): #Этот метод устанавливает соответствующее название данного вызывающего объекта потока

# func - функция запускаемая в потоке; args - аргументы передаваемые в функцию, т.к это кортеж если один аргумент, должна быть запятая; name - нвзвание потока, daemon - устанавливаем поток-демон
thr1 = threading.Thread(target=func, args=(1,), name='Поток-1', daemon=False) # создание потока 
thr1.start() - #запуск потока
thr1.join() - #ожидает завершения

# процесс - это основная программа

# процессы могут выполняться параллельно, потоки последовательно
# 1 поток лучше чем 100, т.к интерпретатор будет переключаться между ними долго

'''Поток-демон — это поток, который выполняет задачи в фоновом режиме. Потоки-демоны полезны для выполнения задач, которые не являются критическими. Программа не ждет завершения работы потока-демона перед завершением. При завершении программы поток-демон автоматически завершается.'''

thr1.setDaemon(True)

locker = threading.Lock() # создает объект блокировщика
locker.acquire() # заблокировать досткп остальным потокам
# между ними может отбработать только один поток(первый запущенный), остальным запрещено
locker.release() # освободить данную область

with locker: # краткая запись с locker.acquire() по locker.release()
  some code...

Lock() # может быть заблокирован и раблокирован из любого потока
Rlock() # может быть заблокирован только тот поток, который блокировал

# Lock и  Rlock удобнее использовать когда не сколько потоков идут по одной функции

threading.Timer(interval, func) # interval - время ожидания до запуска потока, func - функция используемая в потоке
thr1.cancel() # отменить поток до истечения вреемени ожидания interval

data = threading.local() # позволяет хранить данные в наших потоках

def get(): # функция вне потока, нозапускается внутри потоков
  print(data.value)

def t1():
  data.value = 111 # value - доступен только в эотм потоке
  get()

def t1():
  data.value = 222
  get()

local() # доступно внутри функции, которая внутри потока

# Семафоры

# к примеру есть 10 потоков, счетчик = 5, значит сначало пройдут 5 потоков, а остальные будут в очереди, как только освободиться место под один пото, сразу же запуститься следующий

from threading import Thread, BoundedSemaphore, currentThread
import time

max_connection = 5 # макс. количество потоков, работающих одновременно
pool = BoundedSemaphore(value=max_connection)

def test():
  with pool: # блокировка как с locker
    print(currentThread().name)
    time.sleep(6)

for i in range(10):
  Thread(target=test, name=f'thr-{i}').start()


# Барьеры
  
import time
import threading
import random

def test(barrier):
  slp = random.randint(1, 7)
  time.sleep(slp)
  print(f'Поток [{currentThread().name}] запущен в ({time.ctime()})')
  barrier.wait()
  print(f'Поток [{currentThread().name}] преодолел барьер в ({time.ctime()})')

bar = threading.Barrier(5) 
for i in range(10):
  threading.Thread(target=test, args=(bar, ), name=f'thr{i}').start()
# потоки запускаются, затем они попдают в wait(), когда все потоки вызовут wait(), тогда мы продолжим выполнениек кода
  
## очередь с приоритетами

get()#: Данный метод возвращает следующий элемент вызывая объект queue и удаляя его из этого объекта queue

put()#: Этот метод добавляет новый элемент в данный вызываемый объект queue

qsize()#: Этот метод возвращает общее число текущих элементов в данном вызываемом объекте queue (то есть его размер).

empty()#: Такой метод возвращает некое Булево значение, указывающее является ли вызываемый объект queue пустым.

full()#: Данный метод возвращает некое Булево значение, указывающее является ли вызываемый объект queue заполненным.

#  Может дать больше преимуществ наличие фиксированного числа потоков (обычно именуемого неким пулом потоков), который мог бы работать с имеющимися задачами на основе кооперации.


import multiprocessing

lock = multiprocessing.Lock()

def get_value(l): # тут блокировщик нужно обязательно передавать в параметры фукции
  l.acquire() # так как его вызвал первый поток, он тут и отработает, остальные сюда не зайдут. Можно использовать, если тут что то не очень важно(а вот если бд, то будут проблемы)
  pr_name = multiprocessing.current_process().name
  print(f'Процесс [{pr_name}] запущен')

multiprocessing.Process(target=get_value, args=(lock,))
multiprocessing.Process(target=get_value, args=(lock,))
# RLock используется по аналогии с RLock в потоках


# Array в multiprocessing
import multiprocessing
import random

def add_value(locker, array, index):
  with locker:
    num = random.randint(0, 5)
    vtime = time.ctime()
    array[index] = num
    print(f'array[{index}] = {num}, sleep = {vtime}')
    time.sleep(num)


lock = multiprocessing.Lock()
arr = multiprocessing.Array('i', range(10))
process = []

for i in range(10):
  pr = multiprocessing.Process(target=add_value, args=(lock, arr, i, ))
  process.append(pr)
  pr.start()

for i in process:
  i.join()

print(list(arr))

# Queue в multiprocessing

import multiprocessing

def get_text(q):
  val = random.randint(0, 10)
  q.put(str(val))  # добавляем элемент в очередь 

queue = multiprocessing.Queue()
pr_list = []

for _ in range(10):
  pr = multiprocessing.Process(target=get_text, args=(queue, ))
  pr_list.append(pr)
  pr.start() 

for i in pr_list:
  i.join()

for elem in iter(queue.get, None): # получаем все значения из очереди
  print(elem)

queue.get() - # получить элемент из очередь
# добавлять и получать значения из очереди можно из любого потока

if __name__ == '__main__': # без него многопроцессорность не работает


## multiprocessing pool
  
import multiprocessing
import random

def end_func(response):
  print('Задание завершено!')
  print(response)

def get_value(value):
  name = multiprocessing.current_process().name
  print(f'[{name}] value: {value}')
  return value  

if __name__ == '__main__':
  with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p: 
    p.map(get_value, list(range(100)))
    p.map_async(get_value, list(range(100)), callback=end_func) # позволяет после всех процессов запустить callback(возвращает результат выполнения)
    p.close() # закрыть пулл
    p.join() # дождаться всех процессов в пулле
# multiprocessing.cpu_count() * 3 - количество ядер процессора. 3 это адекватный множитель(он может быть любым в пределах разумного)
# multiprocessing.Pool(multiprocessing.cpu_count() * 3) - макс. возможное количество процессов
    
# Пуллы могут применяться для парсинга. Типо каждый отдельный процесс парсит отдельную страницу сайта. Например: парсим цену товара из 1000 страниц и в конце callback'ом все результаты в файл
    

    

import multiprocessing
import random

def end_func(response):
  print(response)

def out(x):
  print(f'value: {x}')

if __name__ == '__main__':
  with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p: 
    for i in range(10):
      p.apply_async(out, args=(i,), callback=end_func) # вызовет callback после срабатывания дной функции
    p.close()
    p.join()

Если у нас есть функция с несколькими аргументами: def out(x, y, z): ....

p.starmap(out, [(1,2,3), (4,5,6)], (7,8,9)) # имеет кортеж значений для каждого параметра
p.starmap_async # также в конце вызывает callback


## event, condition

import random
import time
from multiprocessing import Process, Event

event = Event()

def test():
  print('функция запущена')
  while True:
    event.wait() # остановит выполнения нашего event
    print('test')
    time.sleep(1)

def test_event():

  while True:
    event.wait() # остановит выполнения нашего event
    print('test')
    time.sleep(2)
    event.set() # установить наш event в true
    print('event true')
    time.sleep(2)
    event.clear() # установить наш event в false
    print('event false')

Process(target=test).start()
Process(target=test_event).start()


import random
import time
from multiprocessing import Process, Condition

cond = Condition()

def f1():
 
  while True:
    with cond:
      # метод раблокировки и блокировки сработают один раз, при новой итерации все сброситься
      event.wait() # остановит выполнения нашего event
      print('Получили событие')
    

def f2():
  for i in range(100):
    if i % 10 == 0:
      with cond:
        cond.notify() # condition в true
    else:
      print(f'f2: {i}')
    time.sleep(1)

Process(target=f1).start()
Process(target=f2).start()

## менеджеры и барьеры в процессах

import random
import time
from multiprocessing import Process, Barrier

def f1(bar):
  name = multiprocessing.current_process().name
  bar.wait() # блокируем все процессы пока у нас не запуститься (5) процессов 
  print('[{name}] - запущено!')

  b = Barrier(5)
  for i in range(5):
    Process(target=f1, args=(b,)).start()


import random
import time
from multiprocessing import Process, Barrier, Manager

def f(m_dict, m_array):
  # присвоили им значения здесь
  m_dict['name'] = 'test'
  m_dict['version'] = '1.0'
  m_array.append(1)
  m_array.append(2)

if __name__ == '__main__':
  with Manager() as m:
    # создали переменные здесь
    d = m.dict()
    l = m.list()
    pr = Process(target=f, args=(d,l,))
    pr.start()
    pr.join()

    print('dict:', d)
    print('list:', l)

    # благодаря менеджерам можно использовать значения из любых процессов, менять их задвать внутри процессов, а далее работать с ними из общего процесса

# файл сервера
import time
from multiprocessing.managers import BaseManager

def get_time():
  return time.time()

BaseManager.register('get', callable=get_time) # 'get' - название, callable - адрес используемой функции, результат выполнения данной функции передается клиенту
manager = BaseManager(address=('', 4444), authkey=b'abc') # передаем адрес и порт, который будет использоваться в качестве сервера и authkey - пароль для авторизации
server = manager.get_server() # получаем сервер
print('server start')
server.serve_forever() # запускаем его для обработки

# файл клиента
import time
from multiprocessing.managers import BaseManager

BaseManager.register('get')
manager =  BaseManager(address=('127.0.0.1', 4444), authkey=b'abc')
print('client connected')
manager.connect() # подключаемся к нашему процессу

res  = manager.get()
print('result:', res)
# далее запускаем файл с сервером
# затем файл с клиентом


## общение между процессами, использования pipe
import time
from multiprocessing.managers import Pipe

def send_data(conn):
  conn.send('hello world') # отправляет данные используя канал input_c
  conn.close() # закрываем input_c. Это работает только для данной области

def send_data2(conn): # Если сразу закрыть канал, то мы можем только отправлять данные, но получать нет 
    conn.close() 
    conn.send('hello world')

if __name__ == '__main__':
  output_c, input_c = Pipe() # output_c - для передачи данных, input_c - для принятия
  p = multiprocessing.Process(target=send_data, args=(input_c,))
  p.start()
  p.join()
  print('data:', output_c.recv)


import time
from multiprocessing.managers import Pipe

def getter(pipe):
  out, inp = pipe
  inp.close()
  while True: 
    try:
      print('data', out.recv()) # блокирующий метод, пока не получим данные, не можем продолжить
    except:
      break

def setter(sequence, input_c): # sequence - список какой нибудь
  for item in sequence:
    time.sleep(item)
    input_c.send(item)
  

if __name__ == '__main__':
  output_c, input_c = Pipe() # output_c - для передачи данных, input_c - для принятия
  g = multiprocessing.Process(target=getter, args=((output_c, input_c),))
  g.start()
  setter([1, 2, 3, 4, 5], input_c)
  output_c.close()
  input_c.close()
  g.join()


   
