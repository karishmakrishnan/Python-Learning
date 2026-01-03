input_list = [10,20,20,5,20,10,909,66,66,90,90,66,66]
counter_dict = dict()
element_count = 0
most_frequent_element = int()

# counter dictionary for getting the count of each element in list
for x in input_list:
    if x in counter_dict:
        counter_dict[x] +=1
    else:
        counter_dict[x] = 1

# Check wich elemet value is higher and that element is most frequent
for x in counter_dict:
    if(counter_dict[x] > element_count):
        element_count = counter_dict[x]
        most_frequent_element = x

print("The most frequently occured elemet is: ",most_frequent_element)