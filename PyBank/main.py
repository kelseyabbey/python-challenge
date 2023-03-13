import pandas as pd
import os
import csv

#read csv
file = os.path.join(r"/Users/kelseyabbey/Documents/Data Analytics/Module 3 Challenge/python-challenge/PyBank/Resources/budget_data.csv")
#import csv file as dataframe
pybank = pd.read_csv(file, encoding = "utf8")

#headers: profit/loss & dates
profit_loss = pybank["Profit/Losses"]
dates = pybank["Date"]

#total months
total_months = len(pybank)

#net total
net_total = pybank["Profit/Losses"].sum()

#average change
average_change = round(((profit_loss[total_months - 1]- profit_loss[0]) / (total_months - 1)),2)

#set variables
greatest_increase = 0
greatest_decrease = 0

for index,nums in enumerate(profit_loss):

    if index < total_months - 1:
        #month to month difference
        difference = profit_loss[index + 1] - profit_loss[index]

        #greatest increase/decrease with month and amount
        if difference > greatest_increase:
            greatest_increase = difference
            date_on_increase = dates[index + 1]

        elif difference < greatest_decrease:
            greatest_decrease = difference
            date_on_decrease = dates[index + 1]

    #for last index
    else:
        difference = profit_loss[index] - profit_loss[index - 1]

        if difference < greatest_decrease:
            greatest_decrease = difference
            date_on_decrease = dates[index + 1]
        elif difference > greatest_increase:
            greatest_increase = difference
            date_on_increase = dates[index + 1]


#output to text file for both read/write
output = os.path.join(r"/Users/kelseyabbey/Documents/Data Analytics/Module 3 Challenge/python-challenge/PyBank/Analysis/Financial_Analysis.txt")
with open(output,"w+") as text:
    text.write(f"\nFinancial Analysis \n---------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Net Total: ${net_total:,}\n")
    text.write(f"Average Change:: ${average_change:,}\n")
    text.write(f"Greatest Increase: {date_on_increase} (${greatest_increase:,})\n")
    text.write(f"Greatest Decrease: {date_on_decrease} (${greatest_decrease:,})\n---------------\n")

#print output to terminal
print(f"Financial Analysis")
print("---------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total:,}")
print(f"Average Change:: ${average_change:,}")
print(f"Greatest Increase: {date_on_increase} (${greatest_increase:,})")
print(f"Greatest Decrease: {date_on_decrease} (${greatest_decrease:,})")
print("---------------")