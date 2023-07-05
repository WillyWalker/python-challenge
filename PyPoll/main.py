# operating system #
import os

# ..\\w.h.walker\\Bootcamp\\Challenges\\python-challenge\\PyPoll\\Resources\\election_data.csv #
import csv

# How to get to the file #
polling_csv = os.path.join( "Resources", "election_data.csv")

with open(polling_csv) as polling_file:

    ## This is our assistant to work with CSVs ##
    csv_reader = csv.reader(polling_file)
    
    ## Keeps track of what list number we're on ##
    rowCount = 0

    ## This function reads the results ##
    def results(votes = "0"):

        ### Keeps track of what list number we're on ###
        rowCount = 0

        ### Starting out for determining winner, no votes###
        name0 = 0
        ###  Candidate Vote Counts ###
        name1 = 0
        name2 = 0
        name3 = 0
        otherCount = 0

        ### Text that don't need code go here ###
        intro = "\nElection Results\n\n-------------------------\n\n"
        conclude = f"\n\n-------------------------\n"


        for row in csv_reader:

            #### Counts how many rows there are ####
            rowCount += 1

            if row[2] != "Candidate":

                if row[2] == "Charles Casper Stockham":
                    name1 += 1
                elif row[2] == "Diana DeGette":
                    name2 += 1
                elif row[2] == "Raymon Anthony Doane":
                    name3 += 1
                else:
                    otherCount += 1


        voteTally = {
            "No One": name0,
            "Charles Casper Stockham": name1,
            "Diana DeGette": name2,
            "Raymon Anthony Doane": name3,
            "Other": otherCount
            }

        votes = rowCount - 1
        voteTotal = f"Total Votes: {votes}\n\n-------------------------\n\n"

        name1Stats = f"Charles Casper Stockham: {round(name1/votes * 100, 3)}% ({name1})\n\n"

        name2Stats = f"Diana DeGette: {round(name2/votes * 100, 3)}% ({name2})\n\n"

        name3Stats = f"Raymon Anthony Doane: {round(name3/votes * 100, 3)}% ({name3})\n\n"

        otherStats = f"Other Candidate(s): {round(otherCount/votes * 100, 3)}% ({otherCount})\n\n"

        winnerCount = name0

        ### Break Apart Dictionary ###
        voteNames = list(voteTally.keys())
        voteVals = list(voteTally.values())

        val = 0
        for val in range(0, 4):
            if winnerCount < voteVals[val + 1]:
                winnerCount = voteVals[val + 1]
                winner = voteNames[val + 1]
            elif winner == voteVals[val + 1]:
                winner = "Tie"

        winner = f"-------------------------\n\nWinner: {winner}"

        ### Prints results on terminal ###
        print(intro, voteTotal, name1Stats, name2Stats, name3Stats, otherStats, winner, conclude) 

        ### Print results onto text file ###
        with open("analysis/electionResult.txt", "a") as file:
            file.write(intro)
            file.write(str(votes))
            file.write(name1Stats)
            file.write(name2Stats)
            file.write(name3Stats)
            file.write(otherStats)
            file.write(winner)
            file.write(conclude)

    ## Call Function. Please be nice to it :) ##
    results()