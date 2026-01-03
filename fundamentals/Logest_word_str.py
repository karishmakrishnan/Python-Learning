words = ["engineer", "data", "python", "transformation", "etl"]
highest_str_position = int()
highest_char_in_str = 0
for x in range(len(words)):
    if(len(words[x]) > highest_char_in_str):
        highest_str_position = x
        highest_char_in_str = len(words[x])

print("Longest word in list: ", words[highest_str_position])
