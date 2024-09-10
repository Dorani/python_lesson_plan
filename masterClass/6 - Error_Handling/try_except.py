#Error Handling:
while True:
    try:
        age = int(input('please enter a number representing your age'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you, inputs are correct!')
        break