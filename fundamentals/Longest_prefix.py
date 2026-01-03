strs = ["flower","flower","flower","flower"]
prefix_str = ""
new_str1 = ""
new_str2 = ""
strs_len = len(strs)
j = 2


if (strs[0] == strs[1]):
    prefix_str = strs[0]
else:
    i = 0
    new_str1 = strs[0]
    new_str2 = strs[1]
    len1 = len(new_str1)
    len2 = len(new_str2)
    # print(new_str1)
    # print(new_str2)
    min_len = int(len1 if len1<len2 else len2)
    # print(min_len)
    while(min_len != 0):
        if(new_str1[i] == new_str2[i]):
            prefix_str = prefix_str + new_str1[i]
            # print(prefix_str)
        i = i + 1
        min_len = min_len - 1
# print(prefix_str)
if(len(strs) == 2):
    print(prefix_str)
else:
    prefix_str_len = int(len(prefix_str))
    n = 2
    while(n <= strs_len-1):
        new_str = strs[n]
        if (new_str == prefix_str):
            prefix_str = prefix_str
        else:
            k = 0
            while(k < prefix_str_len):
                # print(k)
                # print(prefix_str)
                # print(new_str)
                if(prefix_str[k] != new_str[k]):
                    # print(k)   
                    
                    prefix_str = prefix_str[:k]
                    # print(prefix_str)
                    break
                k = k+1
                
        n = n+1
        strs_len = strs_len - 1
    print(prefix_str)



