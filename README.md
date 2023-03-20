# python-challenge
Module 3 Assignment in Python
This Assignment consists of analyzing two csvfiles using python scripts. PyBank script analyses financial dataset and PyPoll analyses election dataset

# PyBank 

  -This script reads the input financial dataset budget_data.csv which is composed of two columns Date and Profit/Losses
  -It helps analyse the records to calculate each of the following values: 
    1.The Total dates and Unique months in the dataset
    2.The net total amount of "Profit/Losses" over the entire period, considering that each odd row as each closing period.
    3.The changes in "Profit/Losses" over the entire period, and then the average of those changes.
    4.The greatest increase in profits(date and amount) amidst all those changes. 
    5.The greatest decrease in profits(date and amount) amidst all those changes. 
  -The script then writes all these analysis into a text file, analysis.txt

# PyPoll 

  -This script reads the input election dataset election_data.csv which is composed of three columns Ballot_Ids(aka Votes), County, Candidate. 
  -It helps analyse the records to calculate each of the following values: 
    1.The total number of votes cast
    2.A complete list of candidates who received votes.
    3.The percentage of votes each of those candidates won and the total number of votes each candidate won.
    4.The Winner of the election based on popular votes.  
  -The script then writes all these analysis into a text file, analysis.txt


# References: https://pythonbasics.org/