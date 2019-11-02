import os
import csv

months=0
total=0
current_month=0
prior_month=0
change_value=0
average_change=0
max_change=0
min_change=0



profit_loss=[]
change=[]
date_data=[]




with open('03-Python_Instructions_PyBank_Resources_budget_data.csv', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:

        # month counter
        months=months + 1

        #total change
        profit_loss.append(int(row[1]))
        total=sum(profit_loss)

        #gather change data
        prior_month=current_month
        current_month=int(row[1])
        change_value=current_month-prior_month
        change.append(change_value)

        #gather date data
        date_data.append(str(row[0]))

    #calc change data and titles   
    change.pop(0)
    date_data.pop(0)
    average_change=round((sum(change)/len(change)),2)

    max_change=max(change)
    max_title=date_data[change.index(max_change)]

    min_change=min(change)
    min_title=date_data[change.index(min_change)]


    
   
    print("Financial Analysis")
    print("-----------------------------------")    
    print(f"Total Months: {months}")
    print(f"Total: ${total}") 
    print(f"Average Change:  ${average_change}") 
    print(f"Greatest Increase in Profits: {max_title} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_title} (${min_change})")

    


    # Write to CSV file: Option 1
    with open("PYBank.csv", 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Total Months', 'Total', 'Average Change', "Greatest Increase Month", "Greatest Increase in Profits", "Greatest Decrease Month", "Greatest Decrease in Profits"])

        # Write the second row
        csvwriter.writerow([months, total, average_change, max_title, max_change, min_title, min_change])

     



    
    