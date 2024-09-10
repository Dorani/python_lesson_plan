#Decorator:

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('!!!!!!')
    return wrap_func


@my_decorator
#super boost a function and adding extra functionality to other functions
def hello(greeting, emoji):
    print(greeting, emoji)


a = my_decorator(hello)
a('hiiiiii', ':)')
