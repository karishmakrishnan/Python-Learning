# convert list of tuples to dictionary
List_of_tuples = [
 ("A", 10),
 ("B", 20),
 ("A", 30),
 ("C", 40),
 ("B", 50)
]
dictionary = {}
for key, value in List_of_tuples:
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]
print("Diectionary from list of tuples:")
print(dictionary)

sentence = "karishma madhu sulo kari madhu"
word_list = sentence.split()

word_occurance = dict()
for word in word_list:
    if word in word_occurance:
        word_occurance[word] += 1
    else:
        word_occurance[word] = 1
print("word occurance in the sentance:")
print(word_occurance)