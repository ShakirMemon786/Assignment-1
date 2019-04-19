import csv
import psycopg2
import sys


try:
  connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
  cursor = connection.cursor()
  
  print("connected")
  
except (Exception, psycopg2.DatabaseError) as error :
  print("database error occured",error)
 
filename =sys.argv[1] 
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cursor.execute(
            "INSERT INTO details VALUES (%s, %s, %s, %s)",
            row)
connection.commit()  
