arr = [3,2,4]
target = 6

seen = set()

for num in arr:
    comp = target - num
    if comp in seen:
        print(comp, num)
        break
    seen.add(num)
