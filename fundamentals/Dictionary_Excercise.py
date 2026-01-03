# Task 1
person  = {
    "name":"Alice",
    "age": 25,
    "city": "Delhi"
}

print(f"The Name: {person['name']}")
print(f"The Age: {person['age']}")

# Task 2
student = {
    "name": "Ravi",
     "marks": 85
}
print("\n")
print("Task 2")
student.update({"subject": "Math"})
student.update({"marks": 90})
print(student)

#Task 3
print("Task 3")
product = {
    "id" : 101,
    "name" : "Laptop",
    "price" : 50000

}
print(product)
product.pop("price")
print(product)

# Task 4
# Loop through dictioanries
data = {
    "A": 10,
    "B": 20,
    "C": 30
}

for x in data:
    print(f"Key: {x} Value: {data[x]}")

# Task 5

student = {
    "name": "sara",
    "scores": [80,75,92]
}
grt_mark = 0
for x in student:
    if (x == "scores"):
        marks = student[x]
        for y in range(len(marks)):
            if (marks[y]> grt_mark):
                grt_mark = marks[y]
print(f"Greatest mark:{grt_mark}")

# Task 6

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
dict_fruits = dict()

for fruits in words:
    if fruits in dict_fruits:
        dict_fruits[fruits] += 1
    else:
        dict_fruits[fruits] = 1
print(dict_fruits)

# Task 7

employee = {
    "emp1" : {"name": "John", "salary": 50000},
    "emp2" : {"name": "Meera", "salary": 60000}
}

print(f"Meera's salary:{employee['emp2']['salary']}")

# Task 8 
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
key = ""
d_rev = dict()
for x in d:
    d_rev.update({d[x] : x})
print(d)
print(d_rev)

d1 = {"x": 10, "y": 20}
d2 = {"y": 25, "z": 30}
d3 = dict()

# for x in d1,d2:
#     d3[x] = d1[x]
#     d3[x] = d2[x]
# print(d3)

scores = {
    "A" : 90,
    "B" : 45,
    "C": 88,
    "D": 30
}
print(scores)
grt_scores = dict()
for x in scores:
    if(scores[x]>=60):
        grt_scores.update({x: scores[x]})


print(grt_scores)