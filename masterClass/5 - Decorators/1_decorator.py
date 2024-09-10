#Decorator:

def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('!!!!!!')
    return wrap_func


@my_decorator
#super boost a function and adding extra functionality to other functions
def hello():
    print('hello')

@my_decorator
def bye():
    print('see ya')

hello()
bye()