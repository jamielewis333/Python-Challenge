import os
import csv


cans=str
can_percent=0
votes=0
total_votes=0
max_vote_index=0



cans=[]
unique_cans = [] 
can_votes = []
can_percent_votes = []




with open('03-Python_Instructions_PyPoll_Resources_election_data.csv', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:

        #create voting list with candidates name for vote
                            
        cans.append(row[2])
        

    # get list of unique names 
    for name in cans:              
          
        if name not in unique_cans: 
  
           unique_cans.append(name)  
           

    # get vote count by candidate 
    for name in unique_cans: 
                
        can_votes.append((cans.count(name))) 

    # get vote percentage by candidate 
    for votes in can_votes: 
        total_votes=sum(can_votes)        
        can_percent=round(((votes/total_votes)*100),3)
        can_percent_votes.append(can_percent)

    # print to screen using index placement
    print("Election Results")
    print("--------------------") 
    print(f"Total Votes:  {total_votes}")
    print("--------------------") 
   
    for x in range(len(unique_cans)): 
    
        print(f"{unique_cans[x]}:  {can_percent_votes[x]}%  ({can_votes[x]})")
       
    print("--------------------")

    max_vote_index=can_votes.index(max(can_votes))
    
    print(f"Winner: {unique_cans[max_vote_index]}")
    print("--------------------")
   
    


    # Write to CSV file: Option 1
    with open("PYPoll.csv", 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Candidate Name', 'Total Votes', 'Percent Total Votes']) 
        # Write remaining info
        csvwriter.writerow(unique_cans)
        csvwriter.writerow(can_votes)
        csvwriter.writerow(can_percent_votes)
        csvwriter.writerow(['Winner:']) 
        csvwriter.writerow([unique_cans[max_vote_index]])       
    