# lamda function

sum  = lambda a, b: a+b

print(sum(10,20))

# lamda inside another function
def myfunc(n):
  return lambda a : a * n

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# The map() function applies a function to every item in an iterable:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# The filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# custom sorting using lamda and sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)