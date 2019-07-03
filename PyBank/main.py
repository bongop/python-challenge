# Using a single open
# --------Peter Holder HW3 Python (PyBank)-------------------- 
# This program analyzes Financial Data for my company
import csv
csvpath = "../Resources/budget_data.csv"
#File import and opening
with open (csvpath, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
#Skip the header move to the first row of data
    header_row = next(csv_reader)
    total_profit_loss = 0
    max_incr_profit = 0
    max_decr_profit = 0

# Calculate the total number of months included in the dataset
    budget_data_rows = list(csv_reader)
    total_months = len(budget_data_rows)
    
# Calculate the total amount of "Profit/Losses" over the entire period
    #total_profit_loss = sum(int(row[1]) for row in csv.reader(csv_file))
    first_iteration = True
    delta_list = []
    for row in budget_data_rows:
        curr_pl = float(row[1])
        total_profit_loss = total_profit_loss + curr_pl
        if first_iteration == True:
            prev_pl = curr_pl
            first_iteration = False         
        else:
            delta_pl = curr_pl - prev_pl
            delta_list.append(delta_pl)
            if delta_pl > max_incr_profit:
                max_incr_profit = delta_pl
                max_incr_month = row[0]
            elif delta_pl < max_decr_profit:
                max_decr_profit = delta_pl
                max_decr_month = row[0]
            prev_pl = curr_pl

avg_profit_loss = sum(delta_list) / len(delta_list)

#
print("              Financial Analysis                  ")    
print("--------------------------------------------------")
print(f"The total number of months are:    {total_months}")
print(f"The total_profit_loss is: ${total_profit_loss:.2f}")
print(f"The average profit/loss is: ${avg_profit_loss:.2f}") 
print(f"The maximum profit increase is:{max_incr_month} ${max_incr_profit:.2f}")
print(f"The maximum profit decrease is:{max_decr_month} $({max_decr_profit:.2f})")

f = open('Financial_Analysis.txt', 'w')
f.write("%s\n" % "Financial Analysis")
f.write("%s\n" % "----------------------------")
Total_Months = "Total Months: " + str(total_months) + "\n"
f.write(Total_Months)
tot_pl = "Total: $" + str(int(total_profit_loss)) + "\n"
f.write(tot_pl)
delta_chg = "Average  Change: $" + str(round(avg_profit_loss, 2)) + "\n"
f.write(delta_chg)
max_info = "Greatest Increase in Profits: " + str(max_incr_month) + "  ($" + str(max_incr_profit) + ")\n"
f.write(max_info)
min_info = "Greatest Decrease in Profits: " + str(max_decr_month) + "  ($" + str(max_decr_profit) + ")\n"
f.write(min_info)

f.close()
















# Calculate the average of the changes in "Profit/Losses"over the entire period    
#first_iteration = True

#if first_iteration == True:
#    curr_profit_loss = prev_profit_loss
#    budget_data_rows.append
#else:
#    curr_profit_loss = curr_profit_loss - prev_profit_loss
#    curr_profit_loss = prev_profit_loss    

# Financial Analysis Report print out

    
     
     


    
       

        
   

# Calculate the greatest increase in profits (date and amount) over the entire period





# Calculate the greatest decrease in losses (date and amount) over the entire period