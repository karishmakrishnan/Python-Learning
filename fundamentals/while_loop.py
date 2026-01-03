i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")

# for x in adj:
#     for y in fruits:
#      print(x, y)