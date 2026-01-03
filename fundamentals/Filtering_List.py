scores = [45,89,72,33,90,56]

new_score = list()

scores_len = len(scores)
i = 0

while( i < scores_len):
    if (scores[i] >= 60):
        new_score.append(scores[i])
    i = i+ 1
print(new_score)