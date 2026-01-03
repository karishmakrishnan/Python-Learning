words = ["apple", "ant","banana","ball","car"]
first_letter_group = dict()
wordsList = list()
# my logic
# for x in words:
#     if x[0] not in first_letter_group:
#         first_letter_group[x[0]] = [x]
#     for y in first_letter_group:
#         if y == x[0]:
#             first_letter_group[y] = first_letter_group[y].append(x)
#     # if(x in first_letter_group == x[0] in words):
#     #     list(first_letter_group[x]).append(x)

for w in words:
    key = w[0]
    if key not in first_letter_group:
        first_letter_group[key] = [w]
    else:
        first_letter_group[key].append(w)
print(first_letter_group)

