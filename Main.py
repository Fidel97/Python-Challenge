#dependicies
import os
import csv
#Files to upload
election_csv= os.path.join('Resources/election_data.csv')
total_vote_count= 0
break_line = "------------------------------"
candidate_votes= {}


with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    # first_row= next(csvreader)  
    # # first_row[2] = "cand"
    # # insert key value pair
    # if "cand" not in candidate_votes:
    #     candidate_votes["cand"] = 1
    # else:
    #     candidate_votes["cand"] += 1

    # # increment key value pair
    # # candidate_votes["cand"] += 1
    for row in csvreader: 
        # get the candidate name   
        candidate_name = row[2]    
        # this should increase for each row
        total_vote_count += 1 
        # check if the candidate is in the candidate list
        # if yes, then increase the candidate's vote
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1 

        total_vote_count= sum(candidate_votes.values())
candidate_votes["Charles Percent"] = round((candidate_votes["Charles Casper Stockham"]/total_vote_count) * 100, 3)
candidate_votes["Diana Percent"] = round((candidate_votes["Diana DeGette"]/total_vote_count) * 100, 3)
candidate_votes["Raymon Percent"] = round((candidate_votes["Raymon Anthony Doane"]/total_vote_count) * 100, 3)

winner=max(candidate_votes, key=candidate_votes.get)


print("Election Results")
print(break_line)
print("Total Vote: " + str(total_vote_count))
print("Charles Casper Stockham: " + str(candidate_votes["Charles Percent"]) + "% " + str(candidate_votes["Charles Casper Stockham"]))
print("Diana DeGette: " + str(candidate_votes["Diana Percent"]) + "% " + str(candidate_votes["Diana DeGette"]))
print("Raymon Anthony Doane: " + str(candidate_votes["Raymon Percent"]) + "% " + str(candidate_votes["Raymon Anthony Doane"]))
print(break_line)
print("Winner: " + str(winner))

output_result = os.path.join(".", "analysis", "result.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Total Vote: " + str(total_vote_count) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Charles Casper Stockham: " + str(candidate_votes["Charles Percent"]) + "% " + str(candidate_votes["Charles Casper Stockham"]) + "\n") 
    txt_file.write("Diana DeGette: " + str(candidate_votes["Diana Percent"]) + "% " + str(candidate_votes["Diana DeGette"]) + "\n")
    txt_file.write("Raymon Anthony Doane: " + str(candidate_votes["Raymon Percent"]) + "% " + str(candidate_votes["Raymon Anthony Doane"]) + "\n")
    txt_file.write(break_line + "\n")
    txt_file.write("Winner: " + str(winner) + "\n")
    txt_file.write(break_line + "\n")
