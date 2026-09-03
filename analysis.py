import csv

scores = []

with open("data.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        scores.append(float(row["score"]))

print("Mean score:", sum(scores) / len(scores))
