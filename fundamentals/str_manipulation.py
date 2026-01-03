s = "data engineering"
print(f"s in upper: {s.upper()}")

s_len = len(s)
i = 0
count_e = 0

while (i < s_len):
    if(s[i] == 'e'):
        count_e = count_e+1
    i = i + 1

print(f"The 'e' count is {count_e}")
s_list = s.split()

for i in range(len(s_list)):
    if (s_list[i] == "engineering"):
        s_list[i] = "science"
        

s = s_list[0]+" "+s_list[1]
print(f"after modifying s: {s}")
