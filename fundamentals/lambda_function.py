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