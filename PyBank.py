import os
import csv


# files
budget_data = os.path.join("C:/Users/Owner/Documents/homework",
					   "02-Python_Homework_PyBank_budget_data.csv")
outFile = os.path.join("C:/Users/Owner/Documents/homework", "output.txt")


# variables
months = []
P = []
revenue_change = []
revenue_average = []
month_of_change = []


# Read the 02-Python_Homework_PyBank_budget_data.csv file
with open(budget_data, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvfile)

	# skip header row
	print(f"Header: {csv_header}")

# loop through the data
	for rows in csvreader:
		months.append(rows[0])
		P.append(int(rows[1]))

		# Totaling
		total_months = len(months)
		P = sum(P)
			

# changes of revenue calculations
	for x in range(1, len(P)):
		revenue_change.append((int(P[x]) - int(P[x-1])))
  
		# calculate the average revenue outside of the loop
		revenue_avg = sum(revenue_change) / len(revenue_change)

		# Greatest Increase revenue
		greatestIncrease = max(revenue_change)

		# Greatest Decrease in revenue
		greatestDecrease = min(revenue_change)


# print the outcomes
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(P)))
print("Average Change: " + "$" + str(revenue_average))
print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatestIncrease))
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatestDecrease))


# Write to the text path
file = open("output.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("-----------------------------"+ "\n")
file.write("Total Months: " + str(total_months)+ "\n")
file.write("Total: " + "$" + str(sum(P))+ "\n")
file.write("Average Change: " + "$" + str(revenue_average)+ "\n")
file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatestIncrease)+ "\n")
file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatestDecrease)+ "\n")
file.close()