#The data we need to retrieve:
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os 
#Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a totale vote counter.
total_votes = 0
#candidate options list
candidate_options = []
#candidate votes dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file.
with open(file_to_load) as election_data:
    # to do: read and analyze the data
    file_reader = csv.reader(election_data)
    #read the header row. 
    headers = next(file_reader)
    #print each row to the CSV file
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


#save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")
    print(election_results, end="")
    #save to text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes / float(total_votes)*100)
        candidate_results = (
            f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #save to text file
        txt_file.write(candidate_results)
        
        #determine winner
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = votes_percentage
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


if (votes > winning_count) and (votes_percentage > winning_percentage):
    winning_count = votes
    winning_percentage = votes_percentage
    winning_candidate = candidate_name
        
winning_candidate_summary = (
    f"------------------------\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)
