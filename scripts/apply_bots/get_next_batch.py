import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    batch = []
    for row in reader:
        if len(row) > 8 and row[8].strip() == "TO APPLY":
            batch.append(row)
            if len(batch) == 5:
                break

for i, row in enumerate(batch):
    print(f"{i+1}. {row[0]} | {row[1]} | {row[2]}")
