# palindron substring

string = "abbaeae"

def Palindrom(string):
    str1 = string
    ispalindrom = False
    rev_str = str()
    for i in range(len(str1)-1,0,-1):
        rev_str = rev_str+str1[i]
    if str1 == rev_str:
        ispalindrom = True
    return ispalindrom


