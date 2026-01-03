str1 = input("Enter a string:")
Vowel_Count = 0
Consonant_Count = 0

Lenhth = len(str1)
i = 0

while(i < Lenhth):
    if(str1[i]== 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o'  or str1[i] == 'u'):
        Vowel_Count = Vowel_Count+1
    else:
        Consonant_Count +=1
    i +=1

print("Entered string: ", str1) 
print("Vowel Count: ", Vowel_Count)
print("Consonant count: ", Consonant_Count)

