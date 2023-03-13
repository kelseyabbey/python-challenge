import pandas as pd
import os
import csv

#read csv
file = os.path.join(r"/Users/kelseyabbey/Documents/Data Analytics/Module 3 Challenge/python-challenge/PyPoll/Resources/election_data.csv")
#import csv file as dataframe
pypoll = pd.read_csv(file, encoding = "utf8")

#total votes
total_votes = len(pypoll)

#candidate names and counters
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"
charlescount = 0
dianacount = 0
raymoncount = 0

#variable for vote count
vote_count = pypoll["Ballot ID"]

#loop to add to vote count
for index, row in enumerate(vote_count):
    if pypoll["Candidate"][index] == candidate1:
        charlescount += 1
    elif pypoll["Candidate"][index] == candidate2:
        dianacount += 1
    elif pypoll["Candidate"][index] == candidate3:
        raymoncount += 1

#percentage votes per candidate
candidate1_percent = round((charlescount/total_votes) * 100, 3)
candidate2_percent = round((dianacount/total_votes) * 100, 3)
candidate3_percent = round((raymoncount/total_votes) * 100, 3)

#winner
if charlescount > dianacount and charlescount > raymoncount:
    winner = candidate1
elif dianacount > charlescount and dianacount > raymoncount:
    winner = candidate2
elif raymoncount > charlescount and raymoncount > dianacount:
    winner = candidate3
else:
    winner = "There's a tie!"

#output to text file for both read/write
output = os.path.join(r"/Users/kelseyabbey/Documents/Data Analytics/Module 3 Challenge/python-challenge/PyPoll/Analysis/Election_Results.txt")
with open(output,"w+") as text:
    text.write(f"\nElection Results \n---------------\n")
    text.write(f"Total Votes: {total_votes}\n---------------\n")
    text.write(f"{candidate1}: {candidate1_percent}% ({charlescount})\n")
    text.write(f"{candidate2}: {candidate2_percent}% ({dianacount})\n")
    text.write(f"{candidate3}: {candidate3_percent}% ({raymoncount})\n---------------\n")
    text.write(f"Winner: {winner}\n---------------\n")

#print output to terminal
    print(f"Election Results")
    print("---------------")
    print(f"Total Votes: {total_votes}")
    print("---------------")
    print(f"{candidate1}: {candidate1_percent}% ({charlescount})")
    print(f"{candidate2}: {candidate2_percent}% ({dianacount})")
    print(f"{candidate3}: {candidate3_percent}% ({raymoncount})")
    print("---------------")
    print(f"Winner: {winner}")
    print("---------------")