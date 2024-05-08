###########списки

# индекс   0          1           2          3           4
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

print(food[0])  # выведет pizza
print(food)  # выведет весь список

food[
    2
] = "sushi"  # переопределим элемент по индексу 2, т. е вместо "hotdog" будут "sushi"

food.append("ice cream")  # добавит элемент в конец списка
food.remove("hotdog")  # удалит элемент из списка указанный в скобках
food.pop()  # удалит последний элемент в списке
food.insert(0, "cake")  # встроит по индексу  0 элемент "cake"
food.sort()  # отсортирует список по алфавиту или возрастанию если числа
food.clear()  # удалит все элементы в списке


A = [0] * 1000  # список длинной в 1000 потенциально
C = A  # С это второе имя объекта А. Это не новый объект, а ссылка на старый
С = list(A)  # создаст новый список, копию списка А

# выведем каждый элемент списка в консоль
for i in food:
    print(i)

############# многомерные списки

drinks = ["tea", "coffee", "soda"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)  # выведет весь многомерный список
print(food[0])  # выведет список drinks
print(food[0][2])  # выведет из список drinks элемент soda
