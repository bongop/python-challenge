# Using a single open
# --------Peter Holder HW3 Python (PyPoll)-------------------- 
# This program analyzes Election Results Data 
import csv
import operator  
csvpath = "../Resources/election_data.csv"
#File import and opening
with open (csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    #Skip the header move to the first row of data
    header_row = next(csv_reader)

# Calculate the total number of votes cast
    election_data = list(csv_reader)
    total_votes = len(election_data)

# Determine A complete list of candidates who received votes
    first_iteration = True
#Create a sorted list of the candidates on candidate name    
    candidate_list = sorted(election_data, key=operator.itemgetter(2))

#Intialize a new list to store candidate voting results
election_results = []

hold_candidate = ""
vote_count = 0

#Populate election results list from candidates list who received votes    
for row in candidate_list:
    if first_iteration == True:
        hold_candidate = row[2]
        vote_count += 1
        first_iteration = False         
    elif hold_candidate == row[2]:
        vote_count += 1
    else:
        cand_vote_pct = float(round((vote_count/total_votes)* 100, 3))
        election_results.append([hold_candidate, cand_vote_pct, vote_count])
        hold_candidate = row[2]
        vote_count = 1

# Capture the last candidates voting results and write to election results list
cand_vote_pct = float(round((vote_count/total_votes)* 100, 3))
election_results.append([hold_candidate, cand_vote_pct, vote_count])

election_results = sorted(election_results, key=operator.itemgetter(2), reverse=True)

# Display Election Results to the screen
candidate_votes = 0
winner = ""
print("Election Results") 
print("-------------------------")
print(f"Total Votes: {str(total_votes)} ")
print("-------------------------")
#List out the voting results from the Election Results list
first_iteration = True
Winner = ""
for row in election_results:
    print(f"{row[0]}: {str(float(round(row[1],3)))}% {str(int(row[2]))} ")
    if first_iteration:
        Winner = row[0]
        first_iteration = False
print("-------------------------")
print(f"Winner: {str(Winner)} ")
print("-------------------------")

#Open output file to write election results
f = open('Election_Results.txt', 'w')
f.write("%s\n" % "Election Results")
f.write("%s\n" % "-------------------------")
Total_Votes = "Total Votes: " + str(total_votes) + "\n"
f.write(Total_Votes)
f.write("%s\n" % "-------------------------")
for i, row in enumerate(election_results):
    candidate_line = str(row[0]) + ": " + str(float(round(row[1], 3))) + "% (" + str(row[2]) + ") \n"
    f.write(candidate_line)
f.write("%s\n" % "-------------------------")
winner_line = "Winner: " + Winner + "\n"
f.write(winner_line)
f.write("%s\n" % "-------------------------")

f.close()