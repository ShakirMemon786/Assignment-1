import sys
import psycopg2
def db_insert():
    try:
      connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
      cursor = connection.cursor()
    
      insert_query=""" INSERT INTO
      employe_mobile_detail(id,model,price,first_name,last_name,age,sex,alive,income) VALUES ( '1', 'MInote4', '12000', 'shakir',   'memon', '22', 'm', 'TRUE', '22000')"""
    
      cursor.execute(insert_query)
      connection.commit()
    
      print("record is inserted")

    except (Exception, psycopg2.DatabaseError) as error :
      if(connection):
        print("failed to insert record into employe_mobile_detail",error )
  
    finally:
      if(connection):
        cursor.close()
        connection.close()
      print("postgres connection is closed")   
db_insert()
