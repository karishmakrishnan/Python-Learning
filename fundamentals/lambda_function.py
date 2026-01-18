# lambda function

nums = [1,2,3,4,5,6,7,8,9,10]

def square(nums):
    return nums**2

# map is used to map the given funtion to the values of list, tuple etc

nums_square = list(map(square,nums))
print(nums_square)

# lambda can be used to define functions in a single line code
even = lambda x: x%2 == 0
odd = lambda x: x%2 != 0
# filter is used to filter from the given list by using the logic
nums_even = list(filter(even, nums))
print(nums_even)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(n):
    return n % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers)) 

strings = ["hello", "", "world", "python", "", "filter"]
non_empty_strings = filter(lambda s: s != "", strings)
print(list(non_empty_strings)) # Output: ['hello', 'world', 'python',
# 'filter']

people = [
{"name": "Alice", "age": 25},
{"name": "Bob", "age": 30},
{"name": "Charlie", "age": 35}
]
# Filter people older than 28
older_people = filter(lambda person: person["age"] > 28, people)
print(list(older_people)) # Output: [{'name': 'Bob', 'age': 30}, {'name':'Charlie', 'age': 35}]

values = [0, 1, 2, None, '', 'hello', [], [1, 2], False, True]
filtered_values = filter(None, values)#false, 0, none will be removed from the iterator
print(list(filtered_values)) 
