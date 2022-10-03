#Import modules
import os
import csv
import numpy as np

#Variables Set and Initialization
BallotID_List = []
Candidate_List=[]
Candidate_Unique=[]
Candidate_Count=[]
Analysis_Lines=[]

#Read CSV File

#Specify the file to read from
read_csvpath = os.path.join('Resources', 'election_data.csv')

# Open CSV File
with open(read_csvpath) as csvfile:
    
    # Set CSV Body, comma separated file
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Set CSV Header, comma separated file
    csv_header = next(csvreader)

    #Read CSV Body
    #We convert each column of the file into a list
    for row in csvreader:

        BallotID_List.append(row[0])
        Candidate_List.append(row[2])

#We are converting the Lists created into Numpy arrays to do calcuations with the stored Data.
BallotID_Array= np.array(BallotID_List)
Candidate_Array= np.array(Candidate_List)
#We create 2 different arrays from the candidates one, to differentiate all the unique names and count how many times is it duplicated 
Candidate_Unique, Candidate_Counts = np.unique(Candidate_Array, return_counts=True)

#Append Lines to create Analysis report

#Analysis report Header
Analysis_Lines.append("Election Results")
Analysis_Lines.append('----------------')

#Analysis report Body
#The total amount of votes comes with the size of any List read from the CSV
Analysis_Lines.append("Total Votes: " + str(np.size(BallotID_Array)))
Analysis_Lines.append('----------------')

#For the set of unique values, we read each duplicated and the amount of duplicates it has, plus we define the percentage of items found regarding the total amount of values
for index, items in enumerate(Candidate_Unique):
    Analysis_Lines.append(items + ": " + str('{0:.3f}'.format((Candidate_Counts[index]*100)/np.size(BallotID_Array))) +'% (' + str(Candidate_Counts[index])+")")

Analysis_Lines.append('----------------')

#We look for the highest value on counts, and the index we found we use it to look for the unique name
Analysis_Lines.append("Winner: " + str(Candidate_Unique[np.argmax(Candidate_Counts)]))
Analysis_Lines.append('----------------')

#Specify the file to write to
output_path = os.path.join("analysis", "analysis_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:

    for line in Analysis_Lines:
        #Print each line to TXT File
        f.write(line)
        f.write('\n')
        #Print each line to terminal
        print(line)