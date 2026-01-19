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