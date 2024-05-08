DataMixin - класс который использует повторяющийся функционал в других классах. Мы прописываем его в отдельном файле приложения utils.py

class DataMixin:
  def get_user_context(self, **kwargs):
    context = kwargs
    cats = Category.objects.all()
    context['menu'] = menu
    context['cats'] = cats
    if 'cat_selected' not in context:
      context['cat_selected'] = 0
    return context
  
- Чтобы применить миксин, нужно наследовать его
- В классе в котором применяется миксин:

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs) # берем значение контекста(context_object_name = 'posts') уже существующего
    
    c_def = self.get_user_context(title="Главная страница") # добавляем словарь из повторяющихся свойств
    context = dict(list(context.items()) + list(c_def.items())) # объединяем словари
    return context


- есть миксин LoginRequiredMixin - позволяет ограничить доступ к чему либо не авторизованным пользователям(авторизован если заполнил вошел в админку)

- теперь можно использовать переменную login_url = reverse_lazy('название страницы редиректа') в созданном во views классе

raise_exception = True # выкинет ошибку 403 доступ азпрещен, если не авторизированы


- если используем функции представления, то вешаем декоратор @login_required для ограничения доступа

в DataMixin: 

# делаем копию словаря
user_menu = menu.copy()
# проверяем, если пользователь не авторизован, то удаляем второй элемент списка меню
if not self.request.user.is_authenticated:  
  user_menu.pop(1)

context['menu'] = user_menu

- пагинация:
  содержится в классах представления
  свойство paginate_by = 3 задает количество элементов списка на странице

  если используем функцию представления:
    создаем объект пагинатора paginator = Paginator(spisok, 3) # принмает список и количество элементов списка на странице
    page_number = request.GET.get('page') # получаем номер текущей странице по гет запросу
    page_obj = paginator.get_page(page_number) # список элементов текущей странице

- в html:
  {% for contact in page_obj %} # итератор с помощью которого можно формировать номера страницы
    <p>{{ contact }}</p>
  {% endfor %}

<nav>
  <ul>
    {% for p in page_obj.paginator.page_range %}
      <li>
        <a href="?page={{ p }}">{{ p }}</a>
      <li/>
    {% endfor %}
  </ul>
</nav>

- page_obj.has_other_pages = True # отображает список других страниц(именно range), если False - не покажет список

- page_obj.number|add:-2 # к текущей странице с помощью фильтра add добавляет еще два элемента списка

- if page_obj.has_previous # проверяем есть ли предыдущая страница
- order['id'] - в миксине установит порядок отображения списка, это устранит warning в консоли django