import csv

data = [
    ["Name", "Age"],
    ["Nargis", 22],
    ["Amit", 25]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file saved")