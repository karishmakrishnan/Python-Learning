# Level -1 exercises on lists

lst = [10, 20, 30, 40]

for index, value in enumerate(lst):
    print(f"index {index} -> {value}")
sum = 0
for num in lst:
    sum = sum + num
print("Sum of list elements:", sum)

def even():
    if num% 2 == 0:
        return True
    else:
        return False
even_num = [num for num in lst if even()]
print("Even numbers in list:", even_num)
odd_num = [num for num in lst if not even()]
print("Odd numbers in list:", odd_num)
count_even = 0
count_odd = 0
for num in lst:
    if even():
        count_even += 1
    else:
        count_odd += 1
print("Count of even numbers in list:", count_even)
print("Count of odd numbers in list:", count_odd)

# Level - 2 exercises on lists
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def min_max(list):
    min = float('inf')
    max = float('-inf')
    for num in list:
       if num > max:
          max = num
       if num < min:
          min = num
    return min, max
print("Max in list:", min_max(lst)[1])
print("Min in list:", min_max(lst)[0])

rev_lst = []
for i in range(len(lst)-1, -1, -1):
    rev_lst.append(lst[i])
print("Reversed list:", rev_lst)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common_elements = []
for num in a:
    if num in b:
        common_elements.append(num)
print("Common elements in both lists:", common_elements)
intersect = [x for x in a if x in b]
print("Common elements using list comprehension:", intersect)

# level - 5 exercises on lists
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

k = 3

nested_list = []

for i in range(0, len(L), k):
    sublist = L[i:i+k]
    nested_list.append(sublist)
print("Nested list:", nested_list)

rotate_left = []
rotate = 3
rotate_left = L[rotate:]+ L[:rotate]
print(f"List after left rotation by {rotate}:", rotate_left)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
if is_sorted(l1):
    print("L1 is sorted list")  
if is_sorted(l2):
    print("L2 is sorted list")
# l1_sorted = l1.sort()
# l2_sorted = l2.sort()

# if l1 == l1_sorted:
#     print("L1 is sorted list")

sum_list = []

for i in range(len(l1)):
    sum_list.append(l1[i] + l2[i])
print("Sum of two lists element-wise:", sum_list)

lst = [10, 5, 20, 8]
threshold = 10
filter_list = [num for num in lst if num < threshold]
print(f"Elements in the list less than {threshold}:", filter_list)