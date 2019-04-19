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
  create_table_query = '''CREATE TABLE dict_detail
          ( name varchar(30) NOT NULL,
            department varchar(40) NOT NULL,
            birthdayMonth varchar(40),
            ID varchar(20)); '''
    
  cursor.execute(create_table_query)
  connection.commit()
  print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating details table", error)
    """
    
filename =sys.argv[1]

l=[]
insert_value = "insert into dict_details values"
with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
      l.append(str(tuple(row)))
      
my_tuples = ','.join(l)

insert_value += my_tuples
    cursor.execute(insert_value)
connection.commit()

#with open('details.csv') as csvfile:
#    csvreader = csv.DictReader(csvfile)
#    for row in csvreader:
#      print(row)
#       # print(row[0])
#      print(row['name'],row['department'],row['birthdaymonth'],row['ID'])
"""      
with open('details.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cursor.execute(
            "INSERT INTO details VALUES (%s, %s, %s, %s),(%s, %s, %s, %s))",row
        )
connection.commit()
"""
