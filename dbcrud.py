import psycopg2
from tabulate import tabulate
try:
    connection = psycopg2.connect(user='erp', password='postgres',
                                  host="localhost",
                                  dbname='my_db', port="5432")
    cursor = connection.cursor()
except Exception as error:
    print "please check properly your database its is right or not", error


class dbcrud:
    def db_insert(self):
        num = input("enter number of records you want to insert:")
        my_list = []
        insert_query = """INSERT INTO mobile_detail
                       (id,model,price,first_name) VALUES """
        for i in range(num):

            id = raw_input("enter id which you want to insert: ")
            model = raw_input("enter mobile model: ")
            price = raw_input("enter price of your mobile: ")
            first_name = raw_input("enter your firstname: ")
            my_list.append(str((id, model, price, first_name)))
        my_tuple = ','.join(my_list)
        print "the number of records which we are inserting: \n", my_tuple
        insert_query += my_tuple
        try:
            cursor.execute(insert_query)
        except Exception as e:
            print "enter valid records to insert", e
            return False
        print "record is inserted"

    def db_update(self):

        dict = {
            1: 'id',
            2: 'model',
            3: 'price',
            4: 'first_name',
            }

        my_list = [
            '1 . ID',
            '2 . Model',
            '3 . Price',
            '4 . First_name',
             ]

        for list in my_list:
            print list

        id = input('Enter Id which you want to update :')
        query = "select * from mobile_detail where id = '%s'" % id
        try:
            cursor.execute(query)
            row = cursor.fetchone()
        except Exception as e:
            print"enter valid id for updating record", e

        if not row:
            print "nothing to update"
            return False
        print ("\nID: ", row[0], "\nModel: ", row[1],
               "\nPrice: ", row[2], "\nFirstname: ", row[3], "\n")
        choice = input('Enter your choice what you want to update :')
        while True:
            if choice <= 4:
                value = raw_input('Enter New Value :')
                break
            else:
                print("choose the correct choice")
                choice = input('Enter your choice what you want to update :')

        result = raw_input('are you sure you want to update the record y/n: ')

        if result == 'y':
            update_value = """ update mobile_detail set %s= '%s'
             where id = '%s'""" % (dict[choice], value, id)
            cursor.execute(update_value)
            connection.commit()
            print "record is updated"
            print 'the record which is updated is', row

        elif result == 'n':
            print('ohkk no update is done!!!')

    def db_delete(self):
        row = []
        id = int(raw_input("enter id which you want to delete:"))
        query = "select * from mobile_detail where id = '%s'" % id
        try:
            cursor.execute(query)
            row = cursor.fetchone()
        except Exception as e:
            print"enter valid id", e

        if not row:
            print "Nothing to Delete"
            return False
        print ("\nID: ", row[0], "\nModel: ", row[1],
               "\nPrice: ", row[2], "\nFirstname: ", row[3], "\n")
        result = raw_input('are you sure you want to delete this record y/n: ')
        if result == 'y':
            query = "DELETE FROM mobile_detail WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            print 'record is deleted succesfully'
            print 'the record  which is  deleted is:', row
        elif result == 'n':
            print 'no record is deleted'

    def db_read(self):
        query = """SELECT * FROM mobile_detail ORDER BY id"""
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            print "no such record found to view from the table database", e
        print(tabulate(results,
              headers=['id', ' model', ' price', ' first_name'],
              tablefmt='psql'))
        print "the above records are displayed"


obj = dbcrud()

while True:
    select = raw_input("press 'a' for display the record:\n"
                       "press 'b' for insert new record:\n"
                       "press 'c' for update the record:\n"
                       "press 'd' for delete the record:\n"
                       "press 'n' for exit from operation: ")
    if select == 'a':
        obj.db_read()
    elif select == 'b':
        obj.db_insert()
    elif select == 'c':
        obj.db_update()
    elif select == 'd':
        obj.db_delete()
    elif select == 'n':
        print "exit from the operation!"
        break
    else:
        print("choose the correct option", select)
