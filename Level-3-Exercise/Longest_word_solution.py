string = "Time is an illusion. Lunchtime doubly so!"
remove_puchuation = str.maketrans("","",",.?!';")
clean_string = string.translate(remove_puchuation)
print(clean_string)
clean_string_list = string.split()

long_word = clean_string[0]
long_word_len = len(clean_string[0])

for word in clean_string_list:
    # print(word)
    if (len(word) >= long_word_len):
        long_word = word
        # print(long_word)
        long_word_len = len(word)

print("The longest word in given string is: ", long_word)




