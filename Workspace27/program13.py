# exception handling by try...except statement

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")

try:
    print "Div is:",num_1/num_2
except (ZeroDivisionError):
    print "can not divide by zero !"

# use "raise" keyword to raise custom exception
