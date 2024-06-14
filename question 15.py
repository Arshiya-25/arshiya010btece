import csv
file_path = "demo.csv"
with open(file_path,"r", newline='') as file:
    reader = csv.reader(file)
    print("Data from CSV file:")
    for row in reader:
        print(row)
