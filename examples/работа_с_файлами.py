### Обнаружение файлов

import os

path = "D:\\folder"

if os.path.exists(path):       # есть ли такой путь
    print("Yes")
    if os.path.isfile(path):   # есть ли такой файл?
        print("That is file")
    elif os.path.isdir(path):   # есть ли такая папка?
        print("That is directory")
else:
    print("No")

os.getcwd() # возвращает путь к текущей директории
os.listdir() # возвращает список всех поддирикторий и файлов директории
os.walk() # возвращает генератор, в котором содержится информация о рабочем каталоге
os.path.basename(full_way) # извлечь имя файла из полного пути
os.path.join(file1, file2) # создаем путь, объединяя пути
os.mkdir() # создает новую директорию
    
### открыть и считать содержимое файла

with open("путь", 'режим', encoding='кодировка') as file:
    print(file.read())
    

file = open("путь", 'режим', 'кодировка') # еще один вариант открытия файла
Но в таком случае файл нужно закрывать в конце(освободить память от файла) file.close()

режимы:
    r - открытие на чтение 
    w - открытие на запись
    x - открытие на запись, если файла нет генерируется исключение
    a - открытие на дозапись
    t - открытие в текстовом режиме
    + - открытие на чтение и запись одновременно
    b - открытие в бинарном режиме
режимы можно объединять типо rb, a+, wt и.т.д

file.read() - читает все содержимое файла

file.read(3) - читает первые три символа
Если следом написать еще file.read(2)  - протичает следующие 2 символа
Т.е file.read() перемещает file posotion. Управлять file posotion можно с помощью file.seek()

file.tell() - возвращает номер файловой позиции(file posotion) в байтах

метод readline - построчно считывает строки

метод readlines - взвращает список строк

Обычно информация из файла читают построчно

    
print(file.closed) #проверит закрыт ли файл, если да то вернет True

### Запись в файл 

text = "dfdfdfdfdfdf"

with open("test.txt", "w") as file:
    file.write(text)
    
### добавление в конец файла

text =  "end"

with open("test.txt", "a") as file:
    file.write(text)


### Копирование файла

import shutil     # модуль высокоуровневых файловых операций

shutil.copyfile("test.txt", "C:\\Users\\Name\\Desktop")   # скопируют содержимое test.text на рабочий стол
copy()  #копирует данные файла и режим разрешения файла
copy2() # тоже самое + пытается сохранить метаданные файла.

shutil.copytree() # копирование и перемещение всего содержимого директории

### Перемещение файла 

import os

source = "test.txt"
destination = "C:\\Users\\Name\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("Файл уже там")
    else:
        os.replace(source, destination)       # Как раз само перемещение
        print(source + "переместился")
        
except FileNotFoundError:
    print(source + "не найден")
    

### Удаление файлов

import os
import shutil

path = "folder"

try:
    os.remove(path)        # Удаление файла
    os.rmdir(path)         # удаление пустой папки
    shutil.rmtree(path)    # Удалить все дерево каталогов; путь должен указывать на каталог
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")