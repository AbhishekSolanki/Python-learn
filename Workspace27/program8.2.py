# factorial

def factorial(number):
    result = 1
    while(number>0):
        result = result * number
        number = number - 1
    return result

print factorial(5)
