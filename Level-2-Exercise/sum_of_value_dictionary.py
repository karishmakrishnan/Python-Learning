input_dict = {
    "a":10,
    "b": 20,
    "c": "hello",
    "d": 5
}
sum_value = 0

for x in input_dict:
    if (type(input_dict[x]) == int):
        sum_value +=input_dict[x]

print("Sum of numeric elements in dictionary: ",sum_value)