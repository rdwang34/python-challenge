import os
import csv

pybank_csv = os.path.join("budget.csv")

total_months=[]
total_profits=[]
profit_changes=[]

profits = 0
initial_profit = 0
count=0

with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        count = count + 1
        total_months.append(row[0])
        total_profits.append(row[1])
        profits=profits+int(row[1])

        final_profit= int(row[1])
        monthly_change_profits= final_profit - initial_profit

        profit_changes.append(monthly_change_profits)

        initial_profit = final_profit 
        
        greatest_increase_profits = max(profit_changes)
        greatest_decrease_profits = min(profit_changes)

        increase_date = total_months[profit_changes.index(greatest_increase_profits)]
        decrease_date = total_months[profit_changes.index(greatest_decrease_profits)]

      
    print("Financial Analysis")
    print("---------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(profits))
    print("Average Change: " + "$" + str(sum(profit_changes)/count))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

    with open('analysis.txt','w') as text:
        text.write("Financial Analysis")
        text.write("---------------------------------------")
        text.write("Total Months: " + str(count))
        text.write("Total Profits: " + "$" + str(profits))
        text.write("Average Change: " + "$" + str(sum(profit_changes)/count))
        text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
        text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")







