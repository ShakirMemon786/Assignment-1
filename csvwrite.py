
import csv 
  
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
  
rows = [ ['Nikhil', 'CE', '2', '9.0'], 
         ['Sanchit', 'CE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'EE', '1', '9.5'], 
         ['Prateek', 'ME', '3', '7.8'], 
         ['Sahil', 'EC', '2', '9.1']] 
   
filename = "university_records.csv"
   
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile) 
      
    csvwriter.writerow(fields) 
      
    csvwriter.writerows(rows)

