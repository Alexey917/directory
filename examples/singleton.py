### Паттерн singtone

class DataBase:
    __instance = None
    
    # тут еще переопределяется метод __cal__, но это уже совсем другая история(это нужно чтобы не перезаписывалось значение от последующий созданных объектов)
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            
        return cls.__instance
    
    def __del__(self):
        DataBase.__instance = None
        
# Как я понял это нужно, чтобы у класса был только один экземпляр, елси 
# создается два или более экземпляров, то они будут ссылаться на один и тот же объекты