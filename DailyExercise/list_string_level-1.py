vowels = ['a','e','i','o','u','A','E','I','O','U']
list1 = [11,2,34,5,86,78,90,11,23]
def reverse_string(str1):
    reverse = ''
    for i in range(len(str1)-1,-1,-1):
        reverse = reverse + str1[i]
    return reverse
def vowel_count(str1):
    count = 0
    for char in str1:
        if char in vowels:
            count +=1
    return count
def check_palindrom(str1):
    rev = reverse_string(str1)
    if(str1 == rev):
        print(f"The string {str1} reverse is {rev} and it is palindron")
    else:
        print(f"The string {str1} reverse is {rev} and it is not palindrom")
def length_of_list(list1):
    length = 0
    for x in list1:
        length +=1
    return length
def sum_of_list(list1):
    sum = 0
    for x in list1:
        sum +=x
    return sum

user_string = input("Enter a String: ")
reverse = reverse_string(user_string)
print(f"Reverse of {user_string} is {reverse}")
print(f"The vowels in {user_string} is {vowel_count(user_string)}")
check_palindrom(user_string)
print(f"The length of list is {length_of_list(list1)}")
print(f"The sum of the elements of list is {sum_of_list(list1)}")





