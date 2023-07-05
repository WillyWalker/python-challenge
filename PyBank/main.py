# operating system #
import os

# ..\\w.h.walker\\Bootcamp\\Challenges\\python-challenge\\PyBank\\Resources\\budget_data.csv #
import csv

# How to get to the file #
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as budget_file:

    ## This is our assistant to work with CSVs ##
    csv_reader = csv.reader(budget_file)

    ## This function reads the results ##
    def results(months = "0", total = "0", avgChange = "0", maxPlus = "0", minMinus = "0"):

        ### This introduction is just generic filler, as copied from module instructions. ###
        intro = "\nFinancial Analysis\n\n----------------------------\n\n"

        ### These set counters to 0 ###
        rowCounter = 0

        budgetSum = 0

        first = int(0)
        avgOverall = 0

        maxProf = 0

        minLoss = 0

        ### Calculating Values we want ###
        for row in csv_reader:

            #### General counter ####
            rowCounter += 1
            

            if rowCounter == 2:
                    first = int(row[1])

            #### We only care about data point with number values ####
            if row[1] != "Profit/Losses":

                ##### Sums up profits and losses #####
                budgetSum += int(row[1])

                ##### finds biggest Profit, date and amount #####
                if maxProf < int(row[1]):
                    maxProf = int(row[1])
                    maxProfDate = row[0]

                ##### finds biggest Loss, extracts date and amount #####
                if minLoss > int(row[1]):
                    minLoss = int(row[1])
                    minLossDate = row[0]

        ### Total Months value ###
        valMonths = rowCounter - 1  
        months = f"Total Months: {valMonths}\n\n"

        ### Overall Balance ###
        total = f"Total: ${budgetSum}\n\n"

        ### finds average change per month Part 2 ###
        last = int(row[1])
        avgMos = valMonths - 1
        avgOverall = round((last - first)/ (avgMos), 2)
        avgChange = f"Average Change: ${avgOverall}\n\n"

        ### Biggest Gains ###
        maxPlus = f"Greatest Increase in Profits: {maxProfDate} (${maxProf})\n\n"

        ### Biggest Losses ###
        minMinus = f"Greatest Decrease in Profits: {minLossDate} (${minLoss})\n"
    
        ### Print out results onto Terminal ###
        print(intro, months, total, avgChange, maxPlus, minMinus)

        ### Print out results onto text file ###
        with open("PyBank/analysis/analysisResults.txt", "a") as file:
            file.write(intro)
            file.write(months)
            file.write(total)
            file.write(avgChange)
            file.write(maxPlus)
            file.write(minMinus)

    ## Call Function. Please be nice to it :) ##
    results()