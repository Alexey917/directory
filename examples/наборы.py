#### наборы не упорядоченные и не имеющие индексов элементы. Они быстрее списков и не содеражт повторяющихся элементов

utensils = {"fork", "spoon", "knife"}

dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")                  # добавляет новый элемент  в набор
utensils.remove("fork")                 # удаляет старый элемент из набора      
utensils.clear()                        # очищает весь набор
utensils.update(dishes)                 # обновляет utensils, добавляя в него не повторяющиеся элементы из dishes
dinner_table = utensils.union(dishes)   # объединяет два набора в третий
utensils.difference(dishes)             # выводит элементы не из utensils не схожие с dishes
utensils.intersection(dishes)           # выводит элементы  из utensils схожие с dishes