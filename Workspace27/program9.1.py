def average(A):
    result = 0
    for i in A:
        result = result + i
    return result/len(A)

numbers = [1,2,3,4,5]

print average(numbers)
