import sys
import psycopg2
### for db connection
try:
  connection = psycopg2.connect(user ='erp', password='postgres', host="localhost", dbname = 'my_db', port="5432")
    
  cursor = connection.cursor()
  
  print("connected")
  
except (Exception, psycopg2.DatabaseError) as error :
  print("database error occured",error)
  
class dbcrud:
     ###inserting query  
     def db_insert(self):
       try:
         num=raw_input("enter no:")
         my_list = []
         
         insert_query= "INSERT INTO mobile_detail(id,model,price,first_name) VALUES "
         for i in range(num):
         
           id = raw_input("enter id")
           model = raw_input("enter model")
           price = raw_input("enter price")
           first_name = raw_input("enter first_name")
           my_list.append(str((id,model,price,first_name)))
           print(  "my_list :::", my_list)
         
         my_tuple = ','.join(my_list)
         
         print("\n\n\n my_tuple ::",my_tuple)
         
         
         insert_query += my_tuple
         
         print("\n\n\n Query ::: ", insert_query)
           
        
        
#         insert_query="INSERT INTO mobile_detail(id,model,price,first_name) VALUES (%s,'%s',%s,'%s')"%(id, model, price, first_name)
    
         cursor.execute(insert_query)
         connection.commit()
    
         print("record is inserted")

       except (Exception, psycopg2.DatabaseError) as error :
         if(connection):
           print("failed to insert record into mobile_detail",error )
    
     ###update query   
     def db_update(self):
       try:
         first_name = raw_input("enter name:")
         id = raw_input("enter id:")
         model = raw_input("enter model")
         price = raw_input("enter price")
         
         select =raw_input("a- update by id,\nb update by name,\nc-update by model,\nd update by price:\n")
         
         if select ==a:

         query = "UPDATE mobile_detail SET first_name='%s' WHERE id=%s"%(first_name,id)
         cursor.execute(query)
         connection.commit()
         print("record updated")
       except (Exception, psycopg2.DatabaseError) as error :
         if(connection):
           print("failed to update record into mobile_detail",error )
      
     ###deleting query
     def db_delete(self):
       try:
         id = int(raw_input("enter id to delete:"))
         query = "DELETE FROM mobile_detail WHERE id = '%s'"%(id)
         cursor.execute(query)
         connection.commit()
         print("record is deleted")
       except (Exception, psycopg2.DatabaseError) as error :
         if(connection):
           print("failed to delete record into mobile_detail",error )
  
       
     ####for reading 
     def db_read(self):
       try:
  
         query="""SELECT * FROM mobile_detail"""
        
        
         cursor.execute(query)
         results = cursor.fetchall()
         for row in results:
          id = row[0]
          model = row[1]
          price = row[2]
          first_name = row[3]
          # last_name = row[4]
           #age = row[5]
          # sex = row[6]
          # alive = row[7]
           #income = row[8]
          #print(row)
          print(id,model,price,first_name)
       #  connection.commit()
         print("display record")
       except (Exception, psycopg2.DatabaseError) as error :
         if(connection):
           print("failed to display record into mobile_detail",error )
        
       
obj=dbcrud()
#obj.db_insert()
#obj.db_update()
#obj.db_delete()
#obj.db_read()

dict = {'insert':'obj.db_insert()','update':'obj.db_update()','delete':'obj.db_delete()','read':'obj.read'}

while True:
  select =raw_input("a- for display,\nb for insert,\nc-for update,\nd for delete:\n")

  if select =='a':
   obj.db_read()
  elif select =='b':
   obj.db_insert()
  elif select =='c':
   obj.db_update()
  elif select == 'd':
   obj.db_delete()
  elif select == 'n':
   print("exit from the class!",)
   break 
  else:
   print("choose the correct option",select)





