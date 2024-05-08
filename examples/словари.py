##### словари - это типо как объекты в js

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals["Russia"]                    # получение значеия по ключу "Russia"
capitals.get("Germany")               # получение значения по ключу "Germany" значение = none
capitals.keys()                       # получение всех ключей
capitals.values()                     # получение всех значений
capitals.items()                      # получение всего словаря
capitals.update({"Germany": "Berlin"}) # обновить словарь
capitals.update({"USA": "Las Vegas"})  # обновить словарь
capitals.pop("China")                  # удалить элемент по ключу
capitals.clear()                       #  очистить словарь

# вывод каждого элемента

for key,value in capitals.items():
    print(key,value)