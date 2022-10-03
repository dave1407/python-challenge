#Import modules
import os
import csv
import numpy as np

#Variables Set and Initialization
Profits_Change_Value = 0
Last_Profits_Read = 0
Monthly_Change_List = []
Monthly_Profits_List = []
Monthly_Dates_List = []
Analysis_Lines=[]

#Read CSV File

#Specify the file to read from
read_csvpath = os.path.join('Resources', 'budget_data.csv')

# Open CSV File
with open(read_csvpath) as csvfile:
    
    # Set CSV Body, comma separated file
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Set CSV Header, comma separated file
    csv_header = next(csvreader)
    
    #Read CSV Body
    #We convert each column of the file into a list
    #We also calculate the Monthly change on Profits and make list including each result   
    for row in csvreader:
        #Monthly change on profits calculation
        #We substract actual month's profits to last month's profits
        Profits_Change_Value = int(row[1]) - Last_Profits_Read 
              
        Monthly_Dates_List.append(str(row[0]))
        Monthly_Profits_List.append(int(row[1]))
        Monthly_Change_List.append(Profits_Change_Value)
        
        # We store the actual month's profit into a memory, so in the next scan this will be the last read value
        Last_Profits_Read = int(row[1])

#We are converting the Lists created into Numpy arrays to do calcuations with the stored Data.
Monthly_Profits_Array = np.array(Monthly_Profits_List)

#We removed the first item on the Monthly Change List because during the first period of course there is no change
Monthly_Change_List.pop(0)
Monthly_Change_Array = np.array(Monthly_Change_List)

#Append Lines to create Analysis report

#Analysis report Header
Analysis_Lines.append("Financial Analysis")
Analysis_Lines.append("-----------------------------------------")

#Analysis_report Body, we append the results line by line

#The total count of months in the table should be the actual size of any of the arrays gathering the data from the CSV
Analysis_Lines.append("Total Months: "+ str(np.size(Monthly_Profits_Array)))
#The total profit should be the sum of the Profits/Losses Column, wich we converted to a numpy array
Analysis_Lines.append("Total: $" + str(np.sum(Monthly_Profits_Array)))
#The average change is calculated from the numpy array, we are formatting the output to have only 2 decimals
Analysis_Lines.append("Average Change: $"+'{0:.2f}'.format(np.average(Monthly_Change_Array)))
#The Greatest increase in Profits is just the maximum value found on the numpy array, but we also read the index of such value to find the date on the other list 
Analysis_Lines.append("Greatest Increase in Profits: "+ str(Monthly_Dates_List[(np.argmax(Monthly_Change_List))+1]) + " ($" + str(np.max(Monthly_Change_List))+")")
#The Greatest decrease in Profits is just the minimum value found on the numpy array, but we also read the index of such value to find the date on the other list
Analysis_Lines.append("Greatest Decrease in Profits: "+ str(Monthly_Dates_List[(np.argmin(Monthly_Change_List))+1]) + " ($" + str(np.min(Monthly_Change_List))+")")

#Write TXT File

#Specify the file to write to
output_txtpath = os.path.join("analysis", "analysis_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_txtpath, 'w') as f:

    for line in Analysis_Lines:
        #Print each line to TXT File
        f.write(line)
        f.write('\n')
        #Print each line to terminal
        print(line)
