import os

#Assigning the input csv file name, output text file, and folder for the files to variables and setting paths for them
csvfile = 'budget_data.csv'
datafolder = 'Resources'
output_filename = 'analysis.txt'
output_folder = 'analysis'
#path to collect the data from the csv file in the csvfile folder, path to the textfile to write the output 
budget_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
output_filepath = '{0}/{1}/{2}'.format(os.getcwd(),output_folder,output_filename)

#Initializing the lists for reading the input file data and also for perfoming individual calculations
budgets = []
budget_analysis =[]
change_values = []

#get the month data from date function
def getmonth_fromdate(datestring):
    month_name = datestring.split('-')[0]
    return month_name

#reading the input file as lines 
with open(budget_csv,'r') as csvfilehandle:
     budgetreader = csvfilehandle.readlines()
     i = 0
     for line in budgetreader:
        #skipping the Header record
        if i > 0:           
            line = line.replace('\n','') #replacing the newlines with blank
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            budgets.append(line_array)
         
        i = i + 1


total_record_cnt = len(budgets) #total number of records
i = 0
netchange = 0
netprofit = 0
allmonths =[] #empty list to contain just the months to get unique months later
for budgetrow in budgets:

    #storing current dates, profit/loss data and months 
    current_pf = int(budgetrow[1])
    current_dt = budgetrow[0]
    current_month = getmonth_fromdate(datestring=current_dt)
    allmonths.append(current_month)

    #total profit/loss
    netprofit = netprofit + current_pf

    #calculating net changes only if it is having odds rows which are the period end dates. budget_analysis is a list of final calulated fields
    #storing the changes of profit/loss in another list change_values and calculating the netprofit
    if (i > 0) and (i < total_record_cnt - 1) and (i % 2 != 0): 
        open_pf_ls = int(budgets[i-1][1])
        change_in_pf_ls = current_pf - open_pf_ls
        netchange = netchange + change_in_pf_ls
        budget_analysis.append([current_dt,current_month,current_pf,open_pf_ls,change_in_pf_ls])
        change_values.append(change_in_pf_ls)
    if (i == total_record_cnt -1) and (i % 2 !=0): #for the last record
        open_pf_ls = int(budgets[i-1][1])
        change_in_pf_ls = current_pf - open_pf_ls
        netchange = netchange + change_in_pf_ls
        budget_analysis.append([current_dt,current_month,current_pf,open_pf_ls,change_in_pf_ls])
        change_values.append(change_in_pf_ls) 
    i = i +1

change_values.sort() #sorting the list of change values to calculate the greatest increase and decrease
avg_change = round((netchange * 1.0)/len(change_values),2) #calculating average change
gr_inc_change = change_values[-1]
gr_dec_change = change_values[0]
unique_months = list(set(allmonths)) #set function to fetch all unique months

#fetching the corresponding dates on which greatest increase and decrease of net profit/loss took place
for budgets in budget_analysis:
    if budgets[4] == gr_inc_change:
        date_of_gr_inc = budgets[0]
    if budgets[4] == gr_dec_change:
        date_of_gr_dec = budgets[0]

#creating a message list to write all the calculations into output text file at once.
messages = []
messages.append('Financial Analysis\n')
separator = "-" * 50 
separator = separator + '\n'
messages.append(separator)
messages.append('Total Dates: {0}\n'.format(str(total_record_cnt)))
messages.append('Total unique months: {0}\n'.format(str(len(unique_months))))
messages.append('Total profit/loss : ${0}\n'.format(str(netprofit)))
messages.append('Total change : ${0}\n'.format(str(netchange)))
messages.append('Avg change : ${0}\n'.format(str(avg_change)))
messages.append("Greatest Increase in Profits: {0} (${1})\n" .format(str(date_of_gr_inc),str(gr_inc_change)))
messages.append("Greatest Decrease in Profits: {0} (${1})\n" .format(str(date_of_gr_dec),str(gr_dec_change)))

#prints to the terminal
print('Total Dates: {0}'.format(str(total_record_cnt)))
print('Total unique months: {0}'.format(str(len(unique_months))))
print('Total profit/loss : ${0}'.format(str(netprofit)))
print('Total change : ${0}'.format(str(netchange)))
print('Avg change : ${0}'.format(str(avg_change)))
print("Greatest Increase in Profits: {0} (${1})" .format(str(date_of_gr_inc),str(gr_inc_change)))
print("Greatest Decrease in Profits: {0} (${1})" .format(str(date_of_gr_dec),str(gr_dec_change)))

#writing the final output to the text file analysis.txt
with open(output_filepath, 'w') as outfilehandler:
    outfilehandler.writelines(messages)