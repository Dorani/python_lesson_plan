#Error Handling:

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) :
        print(ZeroDivisionError)


print(sum(1, '2'))
