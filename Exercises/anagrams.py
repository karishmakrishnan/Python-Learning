# check 2 strings are anagrams
str1 = "karishma"
str2 = "makarish"

if len(str1) != len(str2):
    print("Strings are not anagrams")
elif len(str1) == len(str2):
    # sortedstr1 = list(str1).sort()
    sortedstr1 = sorted(str1)
    sortedstr2 = sorted(str2)
    if "".join(sortedstr1) == "".join(sortedstr2):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")
str3 = "ADF pipelines move data efficiently"
str_split = str3.split()
longest_word = ""
for word in str_split:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word in the string is:",longest_word)
print("Longest word in string is:",max(len(word) for word in str_split))