# Basic algorith foundation
lst = [5, 2, 9, 1, 5, 6]
rev = lst [::-1]
print("Original list:", lst)
print("Reversed list:", rev)

max_val = float('-inf')
min_val = float('inf')

for x in lst:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x
print("Maximum value:", max_val)
print("Minimum value:", min_val)

str1 = "malayalam"
is_palindrome = True

rev_str = str1[::-1]
if str1 == rev_str:
    is_palindrome = True
    # print(rev_str)
else:
    is_palindrome = False
print(f"The string '{str1}' is a palindrome: {is_palindrome}")

feq = {}

for num in lst:
    if num not in feq:
        feq[num] = 1
    else:
        feq[num] +=1
print("Frequency of elements in the list:", feq)
