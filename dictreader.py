import csv

with open('dictuniversity_records.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row)
       # print(row[0])
        print(row['name'],row['branch'],row['year'],row['cgpa'],)
