# Second largest number from the list wintout using sort

numbers = [10,20,4,45,99,99,45,100,67,34,23,89,100, 98]

def unique(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique
unique_numbers = unique(numbers)

def second_largest(numbers):
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            second = first
            first = n
        elif n >second and n < first:
            second = n
    return second

print("The second largest number is :", second_largest(unique_numbers))

# Flatten a nested list
nested_list = [[1,2,3],[4,5],[6,7,8,9],[10]]
flat_list = [num for sublist in nested_list for num in sublist]
print("Flattened list is:", flat_list)