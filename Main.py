#dependicies 
import os 
import csv
#Files to Load
budget_csv = os.path.join( 'Resources', 'budget_data.csv')
months =[]
change_list= []
pl=[]
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    first_row= next(csvreader)
    months.append(first_row[0])
    pl.append(int(first_row[1]))
    previous_value= int(first_row[1])

    # Loop through the data
    for row in csvreader:
        
        months.append(row[0])
        pl.append(int(row[1]))
        change= int(row[1])-previous_value
        change_list.append(change)
        previous_value=int(row[1])



avg_change= round(sum(change_list)/len(change_list),2)

max_increase=max(change_list)
min_increase=min(change_list)

max_index=change_list.index(max_increase)
min_index=change_list.index(min_increase)
Max_month=months[max_index+1]
Min_month=months[min_index+1]


budget_output= (
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {len(months)}\n'
f'Total: ${sum(pl)}\n'
f'Average Change: ${avg_change}\n'
f'Greatest Increase in Profits: {Max_month} (${max_increase})\n'
f'Greatest Decrease in Profits: {Min_month} (${min_increase})\n')

print(budget_output)
out_puttext = os.path.join( 'Analysis', 'budget_analysis.txt')
with open(out_puttext, 'w') as textfile:
    textfile.write(budget_output)