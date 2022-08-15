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





print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidates)):
            print(candidates[i] + ": " + str(votes[i]) +"% (" + str(votes[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('analysis.txt', 'w') as text:
    text.write("Election Results")
    text.write("-----------------------------")
    text.write("Total Vote: " + str(count))
    text.write("-----------------------------")
    for i in range(len(set(candidates))):
        text.write(candidates[i] + ": " + str(votes[i]) +"% (" + str(votes[i]) + "))
    text.write("-----------------------------")
    text.write("The winner is: " + winner )
    text.write("-----------------------------")


