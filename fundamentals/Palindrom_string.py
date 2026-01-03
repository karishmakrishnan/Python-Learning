s1 = str()
print("Enter a  string:")
s1 = input()

s1_len = len(s1)
s1_rev = str()
i = s1_len - 1

while( i >= 0):
    s1_rev = s1_rev+s1[i]
    i = i - 1
if (s1 == s1_rev):
    print(f"The entered string is palindrom: {s1}")
else:
    print(f"The entered string is not palindrom: {s1}")

