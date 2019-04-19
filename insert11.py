import csv
import psycopg2
import sys


try:
  connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
  cursor = connection.cursor()
  
  print("connected")
  
except (Exception, psycopg2.DatabaseError) as error :
  print("database error occured",error)
  

def insert(name, department, birthdayMonth, ID):    
#filename =sys.argv[1]


#with open(filename, 'r') as f:
#    reader = csv.reader(f)
#    next(reader)  # Skip the header row.
    
    sql_insert_query = """ INSERT INTO dict_detail('name', 'department', 'birthdayMonth', 'ID') VALUES (%s,%s,%s,%s)"""
    
    insert_tuple = (name, department, birthdayMonth, ID)
    
    
    result  = cursor.execute(sql_insert_query, insert_tuple)

connection.commit()

print("record is inserted")

insert('shakir','xyz','xxx',12)

#insert(name=sys.argv[1],department=sys.argv[2],birthdayMonth=sys.argv[3],ID=sys.argv[4])
