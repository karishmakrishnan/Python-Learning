str1 = "I love data engineering"
str_list = str1.split()
word_reverse  = []
i = len(str_list) - 1
while(i >= 0):
    word_reverse.append(str_list[i])
    i -=1
word_reverse = " ".join(word_reverse)
print("The string in reverse order: ")
print(word_reverse)