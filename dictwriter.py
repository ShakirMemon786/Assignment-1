
import csv 

fields = ['name', 'branch', 'year', 'cgpa'] 
  
mydict =[{'branch': 'CE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'CE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'EE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'ME', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EE', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 
   
filename = "dictuniversity_records.csv"
   
with open(filename, 'w') as csvfile: 
 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    writer.writeheader() 
      
    writer.writerows(mydict) 

