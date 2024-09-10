# Frequency Counter - sameFrequency
# Write a function called sameFrequency. Given two positive integers, find out if the two numbers have the same frequency of digits.

# Your solution MUST have the following complexities:

# Time: O(1)

# Sample Input:

# sameFrequency(182,281) // true
# sameFrequency(34,14) // false
# sameFrequency(3589578, 5879385) // true
# sameFrequency(22,222) // false


def sameFrequency(number1, number2):
    num1 = str(number1)
    num2 = str(number2)

    if len(num1) != len(num2):
        return False
    
    lookup = {}

    for number in num1:
        if number in lookup:
            lookup[number] += 1
        else:
            lookup[number] = 1

    
    for number in num2:
        if(number not in lookup):
            return False
        else:
            lookup[number] -= 1

    return True


# Example usage
print(sameFrequency(182, 281))  # Should print True
print(sameFrequency(34, 14))    # Should print False