import os
import csv

pypoll_csv = os.path.join("election_data.csv")

totalvotes=[]
candidates=[]

votes = 0
actors = 0

with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_reader)

for row in csv_reader:
    count = count+1
    if row[2]not in candidates:     
        candidates.append(row[2])
        count=0
        count = count +1 
    



