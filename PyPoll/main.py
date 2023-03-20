import os

#Assigning the input csv file name, output text file, and folder for the files to variables and setting paths for them
csvfile = 'election_data.csv'
datafolder = 'Resources'
output_filename = 'analysis.txt'
output_folder = 'analysis'

#path to collect the data from the csv file in the csvfile folder, path to the textfile to write the output 
election_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
output_filepath = '{0}/{1}/{2}'.format(os.getcwd(),output_folder,output_filename)

#Using dictionaries to fetch the total votes for each candidate, key is the candidate name here 
#reading and storing all the ballot data into another list for ballots. 
ballots =[]
candidates = {}

#reading the input file as lines 
with open(election_csv,'r') as csvfilehandle:
     csvreader = csvfilehandle.readlines()
     i = 0
     for line in csvreader:
        #skipping the Header record and reading the file into line_array
        if i > 0:
            line = line.replace('\n','')
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            ballots.append(line_array[0]) #number of votes in ballots list
            candidate_name = line_array[2] #preparing the candidate name data to store in candidates dictionaries. Key = Candidate name
            if candidate_name in candidates.keys():
                #calculating the total ballot counts/votes for each candidate 
                ballot_cnts = candidates[candidate_name]
                ballot_cnts = ballot_cnts + 1
                candidates[candidate_name] = ballot_cnts
            else:
                #if candidate name is found as empty then initializing the dictionary
                candidates[candidate_name]=1
         
        i = i + 1

#creating a list candidate_votes to contain candidate, corresponding number of votes, and their percentage of votes compared to total no. of votes
candidates_votes = []
b_cnts = []
for candidate in candidates.keys():
    candidate_ballot_cnt = candidates[candidate]
    candidate_ballot_percent = str(round((candidate_ballot_cnt * 1.0) /(len(ballots) * 1.0),2) * 100) + '%'  
    candidates_votes.append([candidate,candidate_ballot_cnt,candidate_ballot_percent])
    b_cnts.append(candidate_ballot_cnt)

#sorting the total votes for each candidate in asceding order
b_cnts.sort()

#storing the winning and loosing candidates vote count 
highest_ballot_cnt = b_cnts[-1]
lowest_ballot_cnt = b_cnts[0]

#to fetch the corresponding candidate name for the winner and loosing candidate from the candidates_votes list.
for cd in candidates_votes:
    if cd[1] == highest_ballot_cnt:
        winning_candidate = cd[0]
    if cd[1] == lowest_ballot_cnt:
        loosing_candidate = cd[0]


#creating a message list to write all the calculations into output text file at once.
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

#writing the final output to the text file analysis.txt
with open(output_filepath,'w') as outputfilehandler:
     outputfilehandler.writelines(messages)

#Using join function to print all the items in the message list, adding the newline to have them printed in separate lines
print('\n'.join(messages))