#Generators are iterable 


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result




# Generator Usage
def generator_function(num):
    for i in range(num):
        #pause the function, and comes back to it when next is called
        #yield makes it a generator, and it keeps most recent data in memory, see below:
        yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))
print(next(g))
# for item in generator_function(1000):
#     print(item)