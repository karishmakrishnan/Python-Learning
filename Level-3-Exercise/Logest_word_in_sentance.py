#logest word in a sentance

str1 = "Time is an illusion. Lunchtime doubly so!"
str1_list = str1.split()
longest_word = list()

def longWordList(s):
    wordList = list()
    if (len(s) == 0):
        return None
    wordlen = len(s[0])
    for x in s:
        if(len(x) >= wordlen):
            wordList.append(x)
            wordlen = len(x)
    return wordList

def RemovePuchuation(str1):
    str_list_len = len(str1)
    after_removal = list()
    isPunchuation = False
    for word in str1:
        print(word)
        for j in range(len(word)):
            if (word[j] == "." or word[j] == "!"):
                isPunchuation = True
            
        if isPunchuation == False:
            after_removal.append(word)
        isPunchuation = False
    return after_removal            
            
Longest_word_list = longWordList(str1_list)
print("The given list: ", str1)
print("The longest words from given list: ",Longest_word_list)
Remoning_punchuation = RemovePuchuation(Longest_word_list)
print("After removing punchuations: ",Remoning_punchuation[1])



        
    
