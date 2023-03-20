import os
import csv

csvfile = 'election_data.csv'
datafolder = 'Resources'
output_filename = 'analysis.txt'
output_folder = 'analysis'
#path to collect the data from the csv file in the csvfile folder
election_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
output_filepath = '{0}/{1}/{2}'.format(os.getcwd(),output_folder,output_filename)
ballots =[]
candidates = {}
with open(election_csv,'r') as csvfilehandle:
     csvreader = csvfilehandle.readlines()
     i = 0
     for line in csvreader:
        if i > 0:
            line = line.replace('\n','')
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            ballots.append(line_array[0]) #number of votes in an array
            candidate_name = line_array[2]
            if candidate_name in candidates.keys():
                ballot_cnts = candidates[candidate_name]
                ballot_cnts = ballot_cnts + 1
                candidates[candidate_name] = ballot_cnts
            else:
                candidates[candidate_name]=1
         
        i = i + 1


candidates_votes = []
b_cnts = []
for candidate in candidates.keys():
    candidate_ballot_cnt = candidates[candidate]
    candidate_ballot_percent = str(round((candidate_ballot_cnt * 1.0) /(len(ballots) * 1.0),2) * 100) + '%'  
    candidates_votes.append([candidate,candidate_ballot_cnt,candidate_ballot_percent])
    b_cnts.append(candidate_ballot_cnt)

b_cnts.sort()
highest_ballot_cnt = b_cnts[-1]
lowest_ballot_cnt = b_cnts[0]
for cd in candidates_votes:
    if cd[1] == highest_ballot_cnt:
        winning_candidate = cd[0]
    if cd[1] == lowest_ballot_cnt:
        loosing_candidate = cd[0]

messages = []
messages.append('\nElection Results\n')
separator = "-" * 50 
separator = separator + '\n'
messages.append(separator)
messages.append("Total Votes: {0}\n".format(str(len(ballots))))
messages.append(separator)
for elements in candidates_votes:
    messages.append("{0}: {1} ({2})\n".format(elements[0],elements[2],str(elements[1])))
messages.append(separator)
messages.append("Winner: {0}\n".format(winning_candidate))

with open(output_filepath,'w') as outputfilehandler:
     outputfilehandler.writelines(messages)

print('\n'.join(messages))