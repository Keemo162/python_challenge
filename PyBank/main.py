import csv

# Define the path to the CSV file
file_path = "Resources/budget_data.csv"

# Initialize variables to store financial analysis results
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file and perform analysis
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row
    
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Calculate total profit/loss
        total_profit_loss += int(row[1])
        
        # Track profit/loss changes and months
        current_profit_loss = int(row[1])
        if total_months > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])
        previous_profit_loss = current_profit_loss

# Calculate average change in profit/loss
average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

# Find the greatest increase and decrease in profit/loss
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write results to a text file
with open("analysis/financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
