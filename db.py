import sys
import psycopg2
def db_connect():
  
    connection = psycopg2.connect(user =sys.argv[2], password=sys.argv[3], host="localhost", dbname = sys.argv[1], port="5432")
  
  print("connected susscessfullyy")
db_connect()
  
