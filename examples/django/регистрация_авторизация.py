1. во views создаем класс:

  class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm # специальная форма для регистрации пользователей(предусмотрено в django)
    template_name = 'opredelenie/register.html' # шаблон который будем использовать
    success_url = reverse_lazy('login') # куда будем перенаправлены

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
2. в urls приложения прописываем путь:
  path('register', RegisterUser.as_view(), name='register')

3. делаем все необходимые импорты(UserCreationForm, reverse_lazy, CreateView)

4. создаем register.html и в нем помщаем форму(на html)
    
5. В forms.py :

class RegisterUserForm(UserCreationForm):
    #чтобы свои стили применить
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
       
--------------------------------------------------------------------------------------
авторизация

1. Итак, первым делом добавим в файле views.py класс представления, отвечающий за отображение формы авторизации:

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')
  
2. Затем, мы указываем наш шаблон login.html

{% extends 'имя приложения/base.html' %}
 
{% block content %}
<h1>{{title}}</h1>
 
<form method="post">
    {% csrf_token %}
    <div class="form-error">{{ form.non_field_errors }}</div>
 
    {% for f in form %}
    <p><label class="form-label" for="{{ f.id_for_label }}">{{f.label}}: </label>{{ f }}</p>
    <div class="form-error">{{ f.errors }}</div>
    {% endfor %}
    <button type="submit">Войти</button>
</form>
 
{% endblock %}

3. Осталось в файле urls.py связать маршрут login с нашим классом представления:

path('login/', LoginUser.as_view(), name='login'),

Этот же эффект можно получить, определив константу:

LOGIN_REDIRECT_URL = 'нужный нам адрес'

4. в файле forms.py: 

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

5. Следующим шагом, авторизованным пользователям вместо ссылок «Регистрация» и «Войти» будем показывать ссылку «Выйти». Для этого, в шаблоне base.html, добавим следующую проверку:

{% if request.user.is_authenticated %}
<li class="last"> {{user.username}} | <a href="{% url 'logout' %}">Выйти</a></li>
{% else %}
<li class="last"><a href="{% url 'register' %}">Регистрация</a> | <a href="{% url 'login' %}">Войти</a></li>
{% endif %}

6. Пропишем его в файле urls.py:

path('logout/', LoginUser.as_view(), name='logout'),

7. Если теперь обновить страницу сайта, то увидим эту ссылку «Выйти». Создадим для нее функцию представления, так как непосредственного отображения страницы она не предполагает. Эта функция будет иметь вид:

def logout_user(request):
    logout(request)
    return redirect('login')

8. При успешной регистрации пользователя будем автоматически его авторизовывать, что, мне кажется логичным действием. Для этого, в классе RegisterUser переопределим специальный метод form_valid():

def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')