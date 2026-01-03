input_list = [1,2,2,3,3,3]
frequency_counter = dict()

for x in input_list:
    if x in frequency_counter:
        frequency_counter[x] +=1
    else:
        frequency_counter[x] = 1

print("Frequency counter: ", frequency_counter)
