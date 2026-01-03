d1 = {
    "name": "Alice",
    "age": 25
}

d2 = {
    "city": "Delhi",
    "skill": "Python",
    "age": 29
}

for x in d1:
    d2[x] = d1[x]

print("The merged Dictionary: ", d2)
