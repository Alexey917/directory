## декораторы - это функция, которая расширяет функционал другой функции

def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('----------- do something before call-----------')
        res = func()
        print('----------- do something after call-----------') 
        return res
    return wrapper

def some_func():
    print('do something')
    
some_func = func_decorator(some_func)
some_func()

# или упрощенный вариант

@func_decorator
def some_func():
    print('do something')