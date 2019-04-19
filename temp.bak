import sys
import psycopg2
def db_connect():
  try:
    connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE mobile_detail
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           varchar(20)    NOT NULL,
          PRICE         int,
          FIRST_NAME  varchar(20));'''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("table created successfully in postgress ")      
    print("connected")
  except (Exception, psycopg2.DatabaseError) as error :
    print("error occured",error)
  
  finally:
    if(connection):
      cursor.close()
      connection.close()
    print("postgres connection is closed")  
db_connect()
