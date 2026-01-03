def strStr( haystack, needle):
        haystack_len = len(haystack)
        find = str()
        start = int()
        needle_len = len(needle)
        if (haystack_len < len(needle)):
            return -1
        for i in range(haystack_len):
            find = haystack[i:(i+needle_len)]
            if(find == needle):
                start = i
                break
            else:
                start = -1
        return start
print("Find the Index of the First Occurrence in a String: ",strStr("sadbutsad","sad"))
print("Find the Index of the First Occurrence in a String: ",strStr("butsad","sad"))