import mysql.connector as connector

myDB = connector.connect(
    host= 'localhost',
    port=3306,
    user= 'root',
    password='password',
    database='sakila'
)
insert_query = "INSERT INTO actor (first_name, last_name, last_update) VALUES ( %s, %s , CURRENT_TIMESTAMP)"
values = [('Adam', "Avene"), ('Edger', "Edge"), ('Devon', "Dice") ,]

mycursor = myDB.cursor()
# mycursor.execute(insert_query, values)
mycursor.executemany(insert_query, values)
myDB.commit()

print("No. of rows affected", mycursor.rowcount)


mycursor.close()
myDB.close()
