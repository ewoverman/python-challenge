import os
import csv

#path to collect data
budget_csv = os.path.join('budget_data.csv')

count_of_months = 0
total_amount = 0
change = []
master_change = []
date = []

#read in cvs file, go to next row after header
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvfile)
    # print(f"Headers: {csv_header}")

    #read through each row, find count and sum
    for row in csvreader:
        count_of_months +=1

        float_total_budget = float(row[1])
        total_amount += float_total_budget
        # print(row[1])
        # print(total_amount)

        change.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis\n"
          "-------------------\n"
          "Total Months:  ", str(count_of_months), "\n"
          "Total: $", int(total_amount)) 
  
    var_print = "Financial Analysis\n"    
    var_print += "-------------------\n"
    var_print += "Total Months:  " + str(count_of_months) + "\nTotal: $" + str(int(total_amount))
    

    #read through to find avg change, great increase and greatest decrease
    for i in range(1, len(change)):
        master_change.append(change[i] - change[i-1])
        avg_change = sum(master_change)/len(master_change)

        greatest_increase = max(master_change)
        greatest_decrease = min(master_change)
    
        greatest_increase_date = str(date[master_change.index(max(master_change))])
        greatest_decrease_date = str(date[master_change.index(min(master_change))])

    print("Average Change: $",round(avg_change,2),"\n"
            "Greatest Increase in Profits:", greatest_increase_date,"($", int(greatest_increase),")\n"
            "Greatest Decrease in Profits:", greatest_decrease_date,"($", int(greatest_decrease),")\n")

    var_print += "\nAverage Change: $" + str(round(avg_change,2)) + "\n"
    var_print += "Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(int(greatest_increase)) + ")\nGreatest Decrease in Profits: " + greatest_decrease_date +" ($" + str(int(greatest_decrease))+")\n"

f2 = open("PyBank.txt", "w")
f2.write(var_print) ## sample write out a file
f2.close() ## sample close the file
 