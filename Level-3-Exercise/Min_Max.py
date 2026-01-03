# my own min and max function
numbers = [1,4,12,46,88,32,45,78,90]
def Min(numbers):
    min = numbers[0]
    for x in numbers:
        if x < min:
            min = x
    return min
def Max(numbers):
    max = numbers[0]
    for x in numbers:
        if x > max:
            max = x
    return max

print("Min value of given list: ",Min(numbers))
print("Max value of given list: ",Max(numbers))