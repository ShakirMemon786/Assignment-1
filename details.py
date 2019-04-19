import csv
import psycopg2
import sys


try:
  connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
  cursor = connection.cursor()
  
  print("connected")
  
except (Exception, psycopg2.DatabaseError) as error :
  print("database error occured",error)
"""
try:  
  create_table_query = '''CREATE TABLE details
          ( name varchar(30) NOT NULL,
            department varchar(40) NOT NULL,
            birthdayMonth varchar(40),
            ID varchar(20)); '''
    
  cursor.execute(create_table_query)
  connection.commit()
  print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating details table", error)"""
  

#with open('details.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print('Column names are ',", ".join(row))
#            line_count += 1
#        else:
#            print(row[0] , row[1] , row[2], row[3])
#            line_count += 1
#    print('Processed lines are',line_count)

#filename =sys.argv[1]


#with open(filename, 'r') as f:
#    reader = csv.reader(f)
#    next(reader)  # Skip the header row.
#    for row in reader:
#        cursor.execute(
#            "INSERT INTO details VALUES (%s, %s, %s, %s)",
#            row
#        )
#connection.commit()

filename = sys.argv[1]
with open(filename, 'r') as f:
    reader = csv.reader(f)
      #next(reader)
    read = cursor.copy_from(f,table='details',columns=('name','department','birthdayMonth','Id'),sep=',',null='')
    
connection.commit()
print(read)
  



