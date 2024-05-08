1. Во views создаем класс и наследуем его от ListViews, предварительно импортировав его
2. Этот класс будет преобразовывать наши данные из таблиц в списки

class WomenHome(ListView):
  model = Women  # таблица из бд которая будет преобразовываться в список
  template_name = 'имя_приложения/шаблон.html'  # шаблон в котором применяется класс
  context_object_name = 'posts'  # задаем название списка(по умолчанию object_list)
  extra_context = {'title': 'Главная страница'} # задаем статические данные, в данном случае название страницы
  allow_empty = False # если список пустой - страница не найдена

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs) # берем значение контекста(context_object_name = 'posts') уже существующего
    context['menu'] = menu  # создаем новый ключ, который будет хранить в качестве значения список menu
    context['title'] = 'Главная страница' # передача статических данных по ключу
    return context
  
  def get_queryset(self):
    return Women.objects.filter(is_published=True) # позволяет отобразит конкретную информацию из модели Women
  
3. в urls приложения страницу подключаем:
  path('', Women.as_view(), name='home')

*** DetailView аналогичен предыдущему классу. Используется для отображения конкретного контента(например постов)

1. У себя в классе может использовать:
  slug_url_kwarg = 'post_slug' # для применения своего слага(по умолчанию применяется просто slug)

CreateView тоже самое. Используется отображения формы (например добавление постов)

1. Использует form_class = AddPostForm, вместо model = Women - т.е это форма которая будет применина

2. success_url = reverse_lazy('home')  # адрес куда нас перенаправит после добавления статьи