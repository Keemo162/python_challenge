import os
import csv

# Path to the CSV file
file_path = os.path.join("Resources","election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)

    # Count total votes and populate candidates dictionary
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print total votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a text file
output_file = "analysis/election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results have been saved to {output_file}")