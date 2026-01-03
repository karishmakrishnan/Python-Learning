input_str = "I love data engineering and I love python"
str_list = input_str.split(" ")
frequency_dict = dict()

for strs in str_list:
    if strs in frequency_dict:
        frequency_dict[strs] += 1
    else:
        frequency_dict[strs] = 1

print("Frequency of the words in given string: ",frequency_dict)