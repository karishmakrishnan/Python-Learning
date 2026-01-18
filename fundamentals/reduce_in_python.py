# redeuce in python
# reduce in python is used for combain all the values of an iterable into single value
# The function which pass in a reduce function must have only 2 argument and it will iterate over the iterator and reduce into single value
# Basic syntax: reduce(function, iterable, initializer=None)

from functools import reduce

nums = [1,23,4,5,6,7,8,9]

nums_sum = reduce(lambda a, b: a+b, nums, 0)
nums_product = reduce(lambda a,b: a*b, nums, 1)

print(nums_sum)
print(nums_product)
reduce(lambda a, b: a + b, [1, 2, 3, 4])
reduce(lambda a, b: a * b, (1, 2, 3))
reduce(lambda a, b: a + b, {1, 2, 3})
reduce(lambda a, b: a + b, "abcd")
reduce(lambda a, b: a + b, {"a": 1, "b": 2})
reduce(lambda a, b: a + b, {"a": 1, "b": 2}.values())
reduce(lambda a, b: a + b, range(1, 5))
reduce(lambda a, b: a + b, map(int, ["1","2","4"]))
reduce(lambda a, b: a + b, filter(lambda x: x > 2, [1, 2, 3, 4]))
class MyNums:
    def __iter__(self):
        return iter([1, 2, 3])

reduce(lambda a, b: a + b, MyNums())
# usecase
words = ['Hello', 'World', 'This', 'is', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)