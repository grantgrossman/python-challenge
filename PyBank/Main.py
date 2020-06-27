import os
import csv
from datetime import datetime
os.chdir("/Users/Pharaoh/Desktop/python-challenge/PyBank/Resources")
with open('budget_data.csv') as csv_file:
    budget=csv.reader(csv_file,delimiter=",")
    #move past headings
    next(budget)
    #create empty list to compare dates
    dates=[]
    #set value for calculations
    total=0
    highnumber=0
    lownumber=0
    for row in budget:
        #change string to datetime and add to dates list
        dates.append(datetime.strptime(str(row[0]),'%b-%Y'))
        #Net total calculation 
        total+=int(row[1])
        #determine row of greatest increase
        if int(row[1])>highnumber:
            highnumber=int(row[1])
            greatest_increase = row
        #determine row of greatest decrease
        elif int(row[1])<lownumber:
            lownumber=int(row[1])
            greatest_decrease=row
    #calculate months between the two dates 
    monthsbetween=(dates[-1].year-dates[0].year) * 12 + ((dates[-1].month-dates[0].month)+1)
    #calculate average
    average=round(total/monthsbetween,2)
    #results
finances=print(f"""Financial Analysis
----------------------------
Total Months: {monthsbetween}  
Total: ${total} 
Average  Change: ${average} 
Greatest Increase in Profits: {greatest_increase[0]} ({"${:.2f}".format(float(greatest_increase[1]))})
Greatest Decrease in Profits: {greatest_decrease[0]} ({"${:.2f}".format(float(greatest_decrease[1]))})""")
with open("BigBank.txt", "w") as text_file:
    print(finances,file=text_file)




        