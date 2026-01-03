# string functions
# maketran, translate, and replace
import string

str1 = "Hello World"

# if we are giving one argument to maketran it must be a dictionary
table = str.maketrans(str1,"12345678956"," ")
print(table)
print(str1.translate(table))
print(str.maketrans({'a':1,'b':3}))

table = str.maketrans("","","aeiou") #to delete vowels

text = "abc cde"
table = str.maketrans("abce", "1234", " ")
result = text.translate(table)
result2 = str1.translate(table)
print(result,result2)  # "123 321"
