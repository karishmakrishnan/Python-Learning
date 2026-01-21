#  palindron using loop
str1 = "papp"

len_str = len(str1)
right = 0
left = -1
is_palindrom = True

while right < len_str //2:
    if str1[right] != str1[left]:
        is_palindrom = False
        break
    right +=1
    left -=1
print(f"The string {str1} is palindrom: {is_palindrom}")

# Reverse List
list1 = [1,2,3,4,5,6,6,7,8,9]
rev_list = []
i = len(list1) - 1

while(i >= 0):
    rev_list.append(list1[i])
    i -=1
    
print(f"Actual list:",list1)
print("Reverse of list:", rev_list)