student_scores = [12, 1234, 234, 3234, 1212, 234, 3445, 2345, 224, 42323, 425, 342, 43325, 656, 65464, 746, 453]

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
print(max_score == max(student_scores))