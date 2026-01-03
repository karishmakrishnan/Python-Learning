s1 = input("Enter First string: ")
s2 = input("Enter second string: ")
Entered_string = [s1, s2]
if len(s1) != len(s2):
    print("Strings are not anagrams")
else:
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    if str(s1) == str(s2):
        print("The entered stringa are anagrams", Entered_string)
    else:
        print("Entered string are not anagrams ",Entered_string)

