# reverse the word not the charector
str1 = "I love python coding"
reverse_string = list()

str1_list = str1.split()
n = len(str1_list) - 1
# print(n)
while(n >=0):
    # print(n)
    reverse_string.append(str1_list[n])
    n = n - 1

print("Reverse string: ")
for words in reverse_string:
    print(words+" ",end=" ")

