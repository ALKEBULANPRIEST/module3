import csv
import os
loaded_path = os.path.join("election_data.csv")
tosave_path = os.path.join("election_analysis.txt")
totalvote = 0 
candidate_option = []
candidate_vote ={}
winner = ""
winner_vote = 0
winning_percentage = 0
with open (loaded_path) as electiondata:
    reader = csv.reader(electiondata)
    header = next(reader)
    for row in reader:
        totalvote += 1
        candidatename = row[2]
        if candidatename not in candidate_option:
            candidate_option.append(candidatename)
            candidate_vote[candidatename] = 0
        candidate_vote[candidatename] += 1
with open(tosave_path, "w") as txt_file:
   
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvote:,}\n"
        f"-------------------------\n"

    )
    print(election_results, end="")   
    txt_file.write(election_results)
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_vote:
        votes = candidate_vote[candidate_name]
        vote_percentage = float(votes) / float(totalvote) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winner_vote) and (vote_percentage > winning_percentage):
            winner_vote = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winner_vote:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    print(candidate_vote)
    print(candidate_option)
    print(totalvote)
