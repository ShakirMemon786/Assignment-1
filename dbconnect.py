import psycopg2

connection = psycopg2.connect(user = "erp", password ='postgres', host="localhost", dbname = "my_db", port="5432")
  
print("connected susscessfullyy")
