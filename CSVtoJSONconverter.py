import csv
import json

csv_file = 'data_cleaned.csv' #Replace this with the name of your CSV file 
json_file = 'cleaned.json' #Replace this with the name of your JSON file

data = []

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)
 
with open(json_file, 'w') as f:
    json.dump(data, f, indent=2)